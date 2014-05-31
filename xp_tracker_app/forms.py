from django import forms
from xp_tracker_app.models import Story, Task

class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ['story_name', 'time_est']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_name', 'time_est', 'developer', 'iteration', 'story']