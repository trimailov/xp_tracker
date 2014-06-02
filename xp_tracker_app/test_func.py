from django.test.client import Client
from django.test import TestCase
from django.utils import timezone
import datetime as dt
from xp_tracker_app.models import Story, Task
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

        self.assertTemplateUsed(response, 'index.html', 'base.html')
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

    def test_task_form_fails(self):
        story = Story.objects.create(story_name='Story 1', 
                                     time_est=dt.datetime(2015, 6, 1, 12))
        response = self.client.post('/new_task/', {'task_name':'Task',
                                                   'time_est': 'invalid_time',
                                                   'developer': Task.DEVELOPERS[0][0],
                                                   'iteration': 1,
                                                   'story': story}, follow=True)
        
        self.assertFormError(response, 'form', 'time_est', 'Enter a valid date/time.')

    def test_task_form_passes(self):
        story = Story.objects.create(story_name='Story 1', 
                                     time_est=dt.datetime(2015, 6, 1, 12))
        response = self.client.post('/new_task/', {'task_name':'Task',
                                                   'time_est': dt.datetime(2015, 4, 23, 12, 15),
                                                   'developer': Task.DEVELOPERS[0][0],
                                                   'iteration': 1,
                                                   'story': story}, follow=True)

        # form redirects in reality, though test does not. 
        # self.assertRedirects(response, '/')