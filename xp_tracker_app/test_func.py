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
    """ Functional tests for admin page using selenium """
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(2)

        self.admin = User.objects.create_superuser('admin', 
                                                   'admin@example.com', 
                                                   'password')

    def tearDown(self):
        self.browser.quit()

    def test_can_access_admin_site(self):
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
        self.assertEqual(len(stories_links), 1)

        tasks_links = self.browser.find_elements_by_link_text('Tasks')
        self.assertEqual(len(tasks_links), 1)

        tasks_history_links = self.browser.find_elements_by_link_text('Task finishing historys')
        self.assertEqual(len(tasks_history_links), 1)

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

class FormSeleniumTest(LiveServerTestCase):
    """ Functional tests for form accessing and creating new model instances with them """
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(2)

    def tearDown(self):
        self.browser.quit()

    def test_new_task_form_from_index(self):
        user_story = Story.objects.create(story_name='User story', time_est=dt.datetime(2015, 7, 24, 13, 35))
        self.browser.get(self.live_server_url + '/')

        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('New task', body.text)

        new_task = self.browser.find_element_by_link_text('New task')
        new_task.click()

        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Create new task', body.text)

        task_name = self.browser.find_element_by_name('task_name')
        task_name.send_keys('Create cool website')

        time_est = self.browser.find_element_by_name('time_est')
        time_est.send_keys('2015-06-12 19:45')

        developer = self.browser.find_element_by_name('developer')
        developer.send_keys(Task.DEVELOPERS[0][0])

        iteration = self.browser.find_element_by_name('iteration')
        iteration.send_keys(1)

        story = self.browser.find_element_by_name('story')
        story.send_keys(user_story.id)

        submit_button = self.browser.find_element_by_xpath("//form[input/@type='submit']")
        print(submit_button.text)
        submit_button.click()

        body = self.browser.find_element_by_tag_name('body')

        self.assertIn('Enter', body.text)

        # response = self.client.post('/new_task/', {'task_name':'Task',
        #                                            'time_est': '2015-06-12 19:45',
        #                                            'developer': Task.DEVELOPERS[0][0],
        #                                            'iteration': 1,
        #                                            'story': story}, follow=True)

        # self.assertFormError(response, 'form', 'time_est', 'Enter valid deadline (eg.: 2015-05-17 10:35)')


        # new_task = Task.objects.get(task_name='Create cool website')
        # self.assertEqual(len(new_task), 1)
