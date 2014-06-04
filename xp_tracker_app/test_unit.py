import datetime as dt

from django.test import TestCase
from django.utils import timezone

from xp_tracker_app.models import Story, Task, TaskFinishingHistory
from xp_tracker_app.helper import delta_to_time


class StoryTestCase(TestCase):
    """ Unit tests for Story model """
    def setUp(self):
        story = Story.objects.create(story_name="User story",
                             time_est=dt.datetime(2015, 6, 1, 12))

        Task.objects.create(task_name="Task name 1",
                            time_est=dt.datetime(2015, 5, 27, 12),
                            developer='Linus Torvalds',
                            iteration=1,
                            story=story)

        Task.objects.create(task_name="Task name 2",
                            time_est=dt.datetime(2015, 5, 29, 12),
                            developer='Linus Torvalds',
                            iteration=1,
                            story=story)


    def test_story_creates(self):
        story = Story.objects.get(story_name="User story")

        self.assertEqual(story.story_name, "User story")
        self.assertEqual(story.time_est.replace(tzinfo=None), dt.datetime(2015, 6, 1, 12))
        self.assertEqual(story.time_start.date(), dt.date.today())

    def test_time_estimated_method(self):
        # update automatic Story.time_start value
        Story.objects.filter(story_name="User story").update(time_start=dt.datetime(2015, 5, 31, 12))
        story = Story.objects.get(story_name="User story")

        self.assertEqual(story.time_estimated(), '1d 0h 0m 0s')

    # error between naive (time_fin) and aware (time_start) datetime objects
    # trying to enter naive time_start does not help

    # def test_time_spent_method(self):
    #     story = Story.objects.get(story_name="User story")
    #     Task.objects.all().update(time_start=dt.datetime(2015, 5, 20, 12))
    #     tasks = Task.objects.all()

    #     for task in tasks:
    #         task.time_fin = dt.datetime(2015, 5, 25, 12)

    #     self.assertEqual(story.time_spent(), '10d 0h 0m 0s')

class TaskTestCase(TestCase):
    """ Unit tests for Task model """
    def setUp(self):
        Task.objects.create(task_name="Task name",
                            time_est=dt.datetime(2015, 6, 1, 12),
                            developer='Linus Torvalds',
                            iteration=1,
                            story=Story.objects.create(story_name="User story 2",
                                                       time_est=dt.datetime(2015, 6, 1, 12)))


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

    def test_time_estimated_method(self):
        Task.objects.filter(task_name="Task name").update(time_start=dt.datetime(2015, 5, 31, 12))
        task = Task.objects.get(task_name="Task name")
        self.assertEqual(task.time_estimated(), '1d 0h 0m 0s')

    # error between naive (time_fin) and aware (time_start) datetime objects
    # trying to enter naive time_start does not help

    # def test_time_spent_method(self):
    #     task = Task.objects.get(task_name="Task name")
    #     task.time_fin = dt.datetime(2015, 6, 1, 1)
    #     task.time_fin.replace(tzinfo=None)
    #     task.time_start.replace(tzinfo=None)
    #     self.assertEqual(task.time_spent(), '0d 13h 0m 0s')

class TaskFinishingHistoryTestCase(TestCase):
    """ Unit tests for TaskFinishingHistory model """
    def setUp(self):
        # create story which will be associated to tasks
        story = Story.objects.create(story_name="User story 3",
                                     time_est=dt.datetime(2015, 6, 1, 12))

        # create few tasks which will be associated to TaskFinsihingHistory(TFH) table
        task1 = Task.objects.create(task_name="Task name 1",
                            time_est=dt.datetime(2015, 1, 1, 12),
                            developer='Guido von Rossum',
                            iteration=1,
                            story=story)
        task2 = Task.objects.create(task_name="Task name 2",
                            time_est=dt.datetime(2015, 1, 1, 12),
                            developer='Linus Torvalds',
                            iteration=2,
                            story=story)

        TaskFinishingHistory.objects.create(task_id=task1.id, time_fin=timezone.now())
        TaskFinishingHistory.objects.create(task_id=task2.id, time_fin=timezone.now())
        TaskFinishingHistory.objects.create(task_id=task1.id, 
                                            time_fin=timezone.now()+dt.timedelta(weeks=1))
        TaskFinishingHistory.objects.create(task_id=task2.id, 
                                            time_fin=timezone.now()+dt.timedelta(days=1))

    def test_task_multi_finish(self):
        """ Test if TaskFinishingHistory is pointing to the correct Task """
        task1 = Task.objects.get(task_name="Task name 1")
        task2 = Task.objects.get(task_name="Task name 2")

        # 'reverse' ForeignKey access from Task to TaskFinishingHistory
        task1_history = task1.taskfinishinghistory_set.all()
        task2_history = task2.taskfinishinghistory_set.all()

        # assert all History entries are related to the correct Task
        for entry1 in task1_history:
            self.assertEqual(entry1.task_id, task1.id)

        for entry2 in task2_history:
            self.assertEqual(entry2.task_id, task2.id)


class HelpersTestCase(TestCase):
    """ Unit tests for helper functions in helper.py """
    def test_delta_to_time(self):
        time1 = dt.timedelta(1) # 1 day
        time2 = dt.timedelta(0, 1) # 1 sec
        time3 = dt.timedelta(0, 60) # 1 min
        time4 = dt.timedelta(0, 3600) # 1 hour

        self.assertEqual(delta_to_time(time1), "1d 0h 0m 0s")
        self.assertEqual(delta_to_time(time2), "0d 0h 0m 1s")
        self.assertEqual(delta_to_time(time3), "0d 0h 1m 0s")
        self.assertEqual(delta_to_time(time4), "0d 1h 0m 0s")
        self.assertEqual(delta_to_time(time1+time2+time3+time4), "1d 1h 1m 1s")
