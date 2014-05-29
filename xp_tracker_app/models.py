from django.db import models

class Story(models.Model):
    story_name = models.CharField(max_length=200)
    time_est = models.DateField()

    def __str__(self):
        return self.story_name()

class Task(models.Model):
    DEVELOPERS = (
        ('GvR', 'Guido von Rossum'),
        ('LT', 'Linus Torvalds'),
        ('L', 'Laurynas'),
        ('Mar', 'Marius'),
        ('Man', 'Mantas'),
    )

    task_name = models.CharField(max_length=200)
    time_est = models.DateField()
    time_fin = models.DateTimeField(blank=True, null=True)

    developer = models.CharField(max_length=60, choices=DEVELOPERS)
    iteration = models.IntegerField()

    def __str__(self):
        return self.task_name()
