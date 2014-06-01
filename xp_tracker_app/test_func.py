from django.test.client import Client
from django.test import TestCase
from django.utils import timezone
import datetime as dt
from xp_tracker_app.models import Story
from xp_tracker_app.forms import TaskForm

class IndexTest(TestCase):
    """ Functional tests for index page """
    def setUp(self):
        self.client = Client()

    def test_index_exists(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_index_template(self):
        response = self.client.get('/')

        self.assertContains(response, 'Main page')

        if response.context['stories']:
            self.assertContains(response, 'User Stories')
        else:
            self.assertContains(response, 'There are no stories')

        if response.context['tasks']:
            self.assertContains(response, 'Tasks')
        else:
            self.assertContains(response, 'There are no tasks')

class FormTest(TestCase):
    """ Functional tests for forms """
    def setUp(self):
        self.client = Client()

    def test_task_form_opens(self):
        response = self.client.get('/new_task/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'new_task.html', 'base.html')

    def test_story_form_opens(self):
        response = self.client.get('/new_story/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'new_story.html', 'base.html')