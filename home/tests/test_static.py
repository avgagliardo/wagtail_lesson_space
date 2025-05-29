import os
import pytest
from django.contrib.staticfiles.finders import find as find_static
from django.test import LiveServerTestCase
from urllib.request import urlopen


class TestStaticFileServed(LiveServerTestCase):
    def test_static_css_served(self):
        css_path = "css/lesson_space.css"

        # Ensure it exists on disk
        absolute_path = find_static(css_path)
        self.assertIsNotNone(absolute_path, f"{css_path} not found in staticfiles.")

        # Now hit the live test server
        url = f"{self.live_server_url}/static/{css_path}"
        response = urlopen(url)
        content = response.read()
        self.assertEqual(response.getcode(), 200, f"Could not fetch {url}")
        self.assertIn(b"body", content)  # sanity check content is CSS
