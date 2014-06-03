from django import forms
from xp_tracker_app.models import Story, Task

class StoryForm(forms.ModelForm):
    story_name = forms.CharField(label='Story',
                                 error_messages={'required':'Enter User story name'},
                                 widget=forms.TextInput(attrs={'placeholder': 'As a customer, I want cool website...'}))
    time_est = forms.DateTimeField(label='Deadline',
                                   error_messages={'required':'Enter deadline',
                                                   'invalid':'Enter valid deadline (eg.: 2015-05-17 10:35)'},
                                   widget=forms.TextInput(attrs={'placeholder': '2015-08-23 14:28'}))
    class Meta:
        model = Story
        # fields = ['story_name', 'time_est']

class TaskForm(forms.ModelForm):
    task_name = forms.CharField(label='Task',
                                error_messages={'required':'Enter task name'},
                                widget=forms.TextInput(attrs={'placeholder': 'Create cool website...'}))
    time_est = forms.DateTimeField(label='Deadline',
                                   error_messages={'required':'Enter deadline',
                                                   'invalid':'Enter valid deadline (eg.: 2015-05-17 10:35)'},
                                   widget=forms.TextInput(attrs={'placeholder': '2015-08-23 14:28'}))
    developer = forms.ChoiceField(choices=Task.DEVELOPERS,
                                  error_messages={'required':'Select developer from the list'})
    iteration = forms.IntegerField(min_value=1, 
                                   error_messages={'required':'Enter iteration number',
                                                   'invalid':'Iteration value must be greater than 1'})
    story = forms.ModelChoiceField(queryset=Story.objects.all(),
                                   error_messages={'required':'Select associated User sotry'})

    class Meta:
        model = Task
        # fields = ['task_name', 'time_est', 'developer', 'iteration', 'story']
