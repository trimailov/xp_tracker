from django.test import Client
import unittest

class SimpleTest(unittest.TestCase):
    def setUp(self):
        self.c = Client()

    def test_index_exists(self):
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)
