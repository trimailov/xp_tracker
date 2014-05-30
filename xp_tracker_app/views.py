from django.shortcuts import render
from xp_tracker_app.models import Story, Task

def index(request):
    contents = {}
    contents['stories'] = Story.objects.all()
    contents['tasks'] = Task.objects.all()
    return render(request, 'index.html', contents)