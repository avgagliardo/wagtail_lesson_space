import pytest
from django.test import Client
from wagtail.models import Page, Site
from home.models import HomePage, LessonPage

@pytest.mark.django_db
def test_lesson_page_url_resolution():
    client = Client()

    root = Page.objects.get(id=1)
    homepage = HomePage(title="URL Home", slug="url-home")
    root.add_child(instance=homepage)
    homepage.save_revision().publish()

    Site.objects.update_or_create(
        id=1,
        defaults={
            "hostname": "localhost",
            "root_page": homepage,
            "is_default_site": True,
        }
    )

    lesson = LessonPage(
        title="URL Lesson",
        slug="url-lesson",
        subtitle="URL test lesson",
        domain="biology"
    )
    lesson.body = [("paragraph", "URL test body")]
    homepage.add_child(instance=lesson)
    lesson.save_revision().publish()

    response = client.get("/url-lesson/", HTTP_HOST="localhost")
    assert response.status_code == 200
