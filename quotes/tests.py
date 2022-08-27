from django.test import TestCase

import unittest

from django.test import Client

# Due to error django.core.exceptions.ImproperlyConfigured: Requested setting DEFAULT_CHARSET, but settings are not configured.
# Must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.
import sys
sys.path.append('..')
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'anbima_api.settings')
# Loads apps
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# Create your tests here.

class ApiUnitTest(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_response(self):
        # Issue a GET request.
        response = self.client.get('/api/v1/cota')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

    def test_date(self):
        # Issue a GET request.
        response = self.client.get('/api/v1/cota')

        # Check that the rendered context contains date.
        self.assertIn('date', response.content.decode("utf-8"))

    def test_quote(self):
        # Issue a GET request.
        response = self.client.get('/api/v1/cota')

        # Check that the rendered context contains quote.
        self.assertIn('quote', response.content.decode("utf-8"))


if __name__ == '__main__':
    unittest.main()