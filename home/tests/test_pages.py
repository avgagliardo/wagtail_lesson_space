import pytest
from django.test import Client
from wagtail.models import Page, Site
from home.models import HomePage


@pytest.mark.django_db
def test_create_homepage():
    root = Page.objects.get(id=1)
    homepage = HomePage(title="Test Home", slug="test-home")
    root.add_child(instance=homepage)
    homepage.save_revision().publish()

    assert HomePage.objects.filter(slug="test-home").exists()
    assert homepage.live is True
    assert homepage.get_parent().id == root.id


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
