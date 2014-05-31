from django.db import models

def delta_to_time(timedelta):
    """ Converts datetime.timedelta time in seconds to days, hours, minutes """
    days, seconds = timedelta.days, timedelta.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return "{}d {}h {}m {}s".format(days, hours, minutes, seconds)

class Story(models.Model):
    """ User Story model """
    story_name = models.CharField(max_length=200)
    time_start = models.DateTimeField(auto_now_add=True)
    time_est = models.DateTimeField()

    def __str__(self):
        return self.story_name

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

    def __str__(self):
        return self.task_name

    def time_spent(self):
        if self.time_fin:
            return delta_to_time(self.time_fin - self.time_start)

    def time_estimated(self):
        return delta_to_time(self.time_est - self.time_start)
