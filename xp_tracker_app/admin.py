from django.contrib import admin
from xp_tracker_app.models import Story, Task, TaskFinishingHistory

admin.site.register((Story, Task, TaskFinishingHistory))