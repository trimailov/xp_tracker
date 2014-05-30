from django.test.client import Client
from django.test import TestCase
from django.utils import timezone
import datetime as dt
from xp_tracker_app.models import Story

class IndexTest(TestCase):
    """ Functional tests for index page """
    def setUp(self):
        self.c = Client()

    def test_index_exists(self):
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)

    def test_index_template(self):
        response = self.c.get('/')

        self.assertContains(response, 'Main page')

        if response.context['stories']:
            self.assertContains(response, 'User Stories')
        else:
            self.assertContains(response, 'There are no stories')

        if response.context['tasks']:
            self.assertContains(response, 'Tasks')
        else:
            self.assertContains(response, 'There are no tasks')
