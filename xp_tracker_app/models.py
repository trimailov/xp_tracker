from django.db import models
import datetime as dt
from xp_tracker_app.helper import delta_to_time

class Story(models.Model):
    """ User Story model """
    story_name = models.CharField(max_length=200)
    time_start = models.DateTimeField(auto_now_add=True)
    time_est = models.DateTimeField() # deadline

    def __str__(self):
        return self.story_name

    def time_spent(self):
        """ Calculates time spent on story from related tasks """
        spent_sum = dt.timedelta(0)

        story = Story.objects.get(pk=self.id)

        # 'reverse' ForeignKey access from Story to Task
        story_tasks = story.task_set.all() 
        for task in story_tasks:
            if task.time_fin:
                spent_sum += task.time_fin - task.time_start
        return delta_to_time(spent_sum)

    def time_estimated(self):
        return delta_to_time(self.time_est - self.time_start)

class Task(models.Model):
    """ Task model """
    DEVELOPERS = (
        ('Guido von Rossum', 'Guido von Rossum'),
        ('Linus Torvalds', 'Linus Torvalds'),
        ('Laurynas', 'Laurynas'),
        ('Marius', 'Marius'),
        ('Mantas', 'Mantas'),
    )

    story = models.ForeignKey(Story)

    task_name = models.CharField(max_length=200)
    time_start = models.DateTimeField(auto_now_add=True)
    time_est = models.DateTimeField() # deadline
    time_fin = models.DateTimeField(blank=True, null=True)

    developer = models.CharField(max_length=60, 
                                 choices=DEVELOPERS)
    iteration = models.IntegerField()

    def __str__(self):
        return self.task_name

    # returns time spent on a task
    def time_spent(self):
        if self.time_fin:
            return delta_to_time(self.time_fin - self.time_start)

    # returns estimated working time on a task
    def time_estimated(self):
        return delta_to_time(self.time_est - self.time_start)

class TaskFinishingHistory(models.Model):
    """ Model for storing multiple finishing/updating time values for a task """
    task = models.ForeignKey(Task)
    time_fin = models.DateTimeField()

