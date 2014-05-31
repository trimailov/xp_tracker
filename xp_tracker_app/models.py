from django.db import models
from xp_tracker_app.helper import delta_to_time

class Story(models.Model):
    """ User Story model """
    story_name = models.CharField(max_length=200)
    time_start = models.DateTimeField(auto_now_add=True)
    time_est = models.DateTimeField()

    def __str__(self):
        return self.story_name

    def time_spent(self, pk):
        story = Story.objects.get(pk=pk)
        story_tasks = story.task_set.all()
        print(story_tasks)

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

    task_name = models.CharField(max_length=200)
    time_start = models.DateTimeField(auto_now_add=True)
    time_est = models.DateTimeField()
    time_fin = models.DateTimeField(blank=True, null=True)

    developer = models.CharField(max_length=60, choices=DEVELOPERS)
    iteration = models.IntegerField()

    story = models.ForeignKey(Story)

    def __str__(self):
        return self.task_name

    def time_spent(self):
        if self.time_fin:
            return delta_to_time(self.time_fin - self.time_start)

    def time_estimated(self):
        return delta_to_time(self.time_est - self.time_start)
