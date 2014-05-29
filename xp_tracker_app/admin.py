from django.contrib import admin
from xp_tracker_app.models import Story, Task

admin.site.register((Story, Task))