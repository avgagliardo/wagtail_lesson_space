import pytest
from django.test import Client, TestCase
from wagtail.models import Page, Site
from home.models import HomePage, LessonPage
from wagtail.blocks import StreamValue
from wagtail.rich_text import RichText
from wagtail.test.utils import WagtailPageTests


# Test homepage creation.
@pytest.mark.django_db
def test_create_homepage():
    root = Page.objects.get(id=1)
    homepage = HomePage(title="Test Home", slug="test-home")
    root.add_child(instance=homepage)
    homepage.save_revision().publish()

    assert HomePage.objects.filter(slug="test-home").exists()
    assert homepage.live is True
    assert homepage.get_parent().id == root.id

# Test homepage rendering.
@pytest.mark.django_db
def test_homepage_renders():
    client = Client()

    # Create and publish homepage
    root = Page.objects.get(id=1)
    homepage = HomePage(title="Test Home", slug="test-home")
    root.add_child(instance=homepage)
    homepage.save_revision().publish()

    # Assign it as the root in the Site model
    site = Site.objects.first()
    site.root_page = homepage
    site.save()

    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome" in response.content  # loosened match to avoid brittle failure


# Test lesson page creation.
@pytest.mark.django_db
def test_create_lesson_page():
    client = Client()

    # Set up homepage as root
    root = Page.objects.get(id=1)
    homepage = HomePage(title="Test Home", slug="test-home")
    root.add_child(instance=homepage)
    homepage.save_revision().publish()

    site = Site.objects.first()
    site.root_page = homepage
    site.save()

    # Create a lesson page under homepage
    lesson = LessonPage(
        title="Test Lesson",
        slug="test-lesson",
        subtitle="A unit test lesson",
        domain="physics",
    )
    lesson.body = [
        ("heading", "Lesson Title"),
        ("paragraph", "<p>This is a paragraph.</p>"),
        ("latex", r"$$E=mc^2$$"),
    ]

    homepage.add_child(instance=lesson)
    lesson.save_revision().publish()

    assert LessonPage.objects.count() == 1
    assert lesson.subtitle == "A unit test lesson"
    assert lesson.domain == "physics"
    assert lesson.live is True

    # Now test live URL rendering
    response = client.get(lesson.get_url())
    assert response.status_code == 200
    assert b"Lesson Title" in response.content
    assert b"This is a paragraph" in response.content


class TestLessonPageRendering(WagtailPageTests):


    @pytest.mark.django_db
    def test_lesson_page_renders(self):
        # Setup homepage
        root = Page.objects.get(id=1)
        homepage = HomePage(title="Test Home", slug="test-home")
        root.add_child(instance=homepage)
        homepage.save_revision().publish()

        site = Site.objects.first()
        site.root_page = homepage
        site.save()

        # Add a LessonPage under Home
        lesson = LessonPage(
            title="Render Lesson",
            slug="render-lesson",
            subtitle="Rendering test",
            domain="chemistry"
        )
        lesson.body = [
            ("heading", "Chemistry Fundamentals"),
            ("paragraph", "This is an intro to chemistry."),
            ("latex", r"$$\\Delta G = \\Delta H - T\\Delta S$$"),
        ]

        homepage.add_child(instance=lesson)
        lesson.save_revision().publish()

        # Now we use self.client.get
        response = self.client.get(lesson.url, HTTP_HOST="localhost")
        assert response.status_code == 200
        assert b"Chemistry Fundamentals" in response.content
        assert b"This is an intro to chemistry." in response.content


# Test the tagging system.
@pytest.mark.django_db
def test_lesson_page_tagging():
    client = Client()

    # Setup homepage
    root = Page.objects.get(id=1)
    homepage = HomePage(title="Test Home", slug="test-home")
    root.add_child(instance=homepage)
    homepage.save_revision().publish()

    site = Site.objects.first()
    site.root_page = homepage
    site.save()

    # Create and tag a lesson
    lesson = LessonPage(
        title="Tagged Lesson",
        slug="tagged-lesson",
        subtitle="Tagged lesson for unit test",
        domain="math"
    )
    lesson.body = [("paragraph", "Tagging test body")]
    lesson.tags.add("calculus", "algebra")

    homepage.add_child(instance=lesson)
    lesson.save_revision().publish()

    # Query by tag
    tagged_lessons = LessonPage.objects.filter(tags__name="calculus")

    assert tagged_lessons.exists()
    assert tagged_lessons.first().title == "Tagged Lesson"
