import datetime as dt
from django.test import TestCase
from django.utils import timezone
from xp_tracker_app.models import Story, Task


class StoryTestCase(TestCase):
    """ Testing of Story model """
    def setUp(self):
        Story.objects.create(story_name="User story",
                             time_est=(timezone.now() + dt.timedelta(weeks=1)).date())

    def test_story_creates(self):
        story = Story.objects.get(story_name="User story")

        self.assertEqual(story.story_name, "User story")
        self.assertEqual(story.time_est, (timezone.now() + dt.timedelta(weeks=1)).date())

class TaskTestCase(TestCase):
    """ Testing of Task model """
    def setUp(self):
        Task.objects.create(task_name="Task name",
                            time_est=(timezone.now() + dt.timedelta(days=1)).date(),
                            developer='LT',
                            iteration=1)


    def test_new_task_creates(self):
        """ Tests new created task (finishing time should be None) """
        task1 = Task.objects.get(task_name="Task name")

        self.assertEqual(task1.time_est, (timezone.now() + dt.timedelta(days=1)).date())
        self.assertIsNone(task2.time_fin)

    def test_finished_task(self):
        """ Tests task finishing time comparing to estimated. """
        task1 = Task.objects.get(task_name="Task name")
        task1.time_fin = (timezone.now() + dt.timedelta(days=1)).date()

        self.assertEqual(task1.time_fin, task1.time_est)
