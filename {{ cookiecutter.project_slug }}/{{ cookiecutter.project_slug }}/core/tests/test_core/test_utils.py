import unittest.mock
from unittest.mock import MagicMock
from django.test import testcase

from {{ cookiecutter.project_slug }}.core.utils.urls import redirect_next_or_default



class TestUtils(testcase):

    def test_urls(self):
        response = redirect_next_or_default(path="/home/", default="/abcd/")
        self.assertEqual(response.url, "/abcd/")

        response = redirect_next_or_default(
            path="/home/?next=/place/", default="/abcd/"
        )
        self.assertEqual(response.url, "/place/")

        response = redirect_next_or_default(path="/home/?one=/place/", default="/abcd/")
        self.assertEqual(response.url, "/abcd/")