import datetime as dt
from django.test import TestCase
from django.utils import timezone
from xp_tracker_app.models import Story, Task
from xp_tracker_app.helper import delta_to_time


class StoryTestCase(TestCase):
    """ Unit tests for Story model """
    def setUp(self):
        Story.objects.create(story_name="User story",
                             time_est=dt.datetime(2015, 6, 1, 12))

    def test_story_creates(self):
        story = Story.objects.get(story_name="User story")

        self.assertEqual(story.story_name, "User story")
        self.assertEqual(story.time_est.replace(tzinfo=None), dt.datetime(2015, 6, 1, 12))
        self.assertEqual(story.time_start.date(), dt.date.today())

class TaskTestCase(TestCase):
    """ Unit tests for Task model """
    def setUp(self):
        Task.objects.create(task_name="Task name",
                            time_est=dt.datetime(2015, 6, 1, 12),
                            developer='Linus Torvalds',
                            iteration=1)


    def test_new_task_creates(self):
        """ Tests new created task (finishing time should be None) """
        task1 = Task.objects.get(task_name="Task name")

        self.assertEqual(task1.time_est.replace(tzinfo=None), dt.datetime(2015, 6, 1, 12))
        self.assertEqual(task1.time_start.date(), dt.date.today()) 
        self.assertIsNone(task1.time_fin)
        self.assertEqual(task1.developer, 'Linus Torvalds')
        self.assertEqual(task1.iteration, 1)

    def test_finished_task(self):
        """ Tests task finishing time comparing to estimated. """
        task1 = Task.objects.get(task_name="Task name")
        task1.time_fin = dt.datetime(2015, 6, 1, 12)

        self.assertEqual(task1.time_fin.replace(tzinfo=None), dt.datetime(2015, 6, 1, 12))

class HelpersTestCase(TestCase):
    """ Unit tests for helper functions in helper.py """
    def test_delta_to_time(self):
        time1 = dt.timedelta(1) # 1 day
        time2 = dt.timedelta(0, 1) # 1 sec
        time3 = dt.timedelta(0, 60) # 1 min
        time4 = dt.timedelta(0, 3600) # 1 hour

        self.assertEqual(delta_to_time(time1), "1d 0h 0m")
        self.assertEqual(delta_to_time(time2), "0d 0h 0m")
        self.assertEqual(delta_to_time(time3), "0d 0h 1m")
        self.assertEqual(delta_to_time(time4), "0d 1h 0m")
        self.assertEqual(delta_to_time(time1+time2+time3+time4), "1d 1h 1m")
