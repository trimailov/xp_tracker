from django.shortcuts import render, redirect
from xp_tracker_app.models import Story, Task
from xp_tracker_app.forms import StoryForm, TaskForm
from django.utils import timezone

def index(request):
    contents = {}
    contents['stories'] = Story.objects.all()
    contents['tasks'] = Task.objects.order_by('iteration', 'time_est')
    return render(request, 'index.html', contents)

def new_story(request):
    form = StoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'new_story.html', {'form':form})

def new_task(request):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'new_task.html', {'form':form})

def task_finished(request, task_pk):
    task = Task.objects.get(pk=task_pk)
    task.time_fin = timezone.now()
    task.save()
    return redirect('index')
