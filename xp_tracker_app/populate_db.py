import datetime as dt
import random

from django.utils import timezone

from xp_tracker_app.models import Story, Task

""" Module, for populating database during development or testing """

def create_stories():
    for story in range(5):
        Story.objects.create(story_name="User story #%s" % str(story+1),
                             time_est=(timezone.now() + dt.timedelta(weeks=story+1)))

def create_tasks():
    for task in range(30):
        Task.objects.create(task_name="Task #%s" % str(task+1),
                            time_est=(timezone.now() + dt.timedelta(days=task+1)),
                            developer=Task.DEVELOPERS[random.randint(0, 4)][1],
                            iteration=task//6+1, #iterations are from 1 to 5
                            story=Story.objects.get(story_name="User story #%s" % str(task//6+1))
                            )
