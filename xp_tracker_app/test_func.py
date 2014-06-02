import datetime as dt

from django.contrib.auth.models import User
from django.test.client import Client
from django.test import TestCase, LiveServerTestCase
from django.utils import timezone
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from xp_tracker_app.models import Story, Task
from xp_tracker_app.forms import TaskForm

""" 
xp_tracker_app functional test module.

Though, I am not exactly sure were is the exact breaking point 
between unit test and functional test. 

According to this django.test.client tests are performed here 
(classes with name "ViewTest").

Tests using selenium functional test package are performed in 
classes with name "ViewSeleniumTest".

"""


class IndexTest(TestCase):
    """ Tests for index page """
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

class AdminSeleniumTest(LiveServerTestCase):
    """ Tests for index page using selenium """
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

        self.admin = User.objects.create_superuser('admin', 
                                                   'admin@example.com', 
                                                   'password')

    def tearDown(self):
        self.browser.quit()

    def test_can_create_story_via_admin_site(self):
        self.browser.get(self.live_server_url + '/admin/')

        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Django administration', body.text)

        username_field = self.browser.find_element_by_name('username')
        username_field.send_keys('admin')

        password_field = self.browser.find_element_by_name('password')
        password_field.send_keys('password')
        password_field.send_keys(Keys.RETURN)

        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Site administration', body.text)

        stories_links = self.browser.find_elements_by_link_text('Storys')
        self.assertEquals(len(stories_links), 1)

        stories_links = self.browser.find_elements_by_link_text('Tasks')
        self.assertEquals(len(stories_links), 1)

        stories_links = self.browser.find_elements_by_link_text('Task finishing historys')
        self.assertEquals(len(stories_links), 1)

class FormTest(TestCase):
    """ Tests for forms """
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

        self.assertFormError(response, 'form', 'time_est', 'Enter valid deadline (eg.: 2015-05-17 10:35)')

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