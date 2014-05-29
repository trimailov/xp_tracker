from django.db import models

class Story(models.Model):
    story_name = models.CharField(max_length=300)
    time_est = models.DateField()

    def __str__(self):
        return self.story_name()

class Task(models.Model):
    task_name = models.CharField(max_length=300)
    time_est = models.DateField()
    time_fin = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.task_name()
