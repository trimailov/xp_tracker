from django.shortcuts import render, redirect
from xp_tracker_app.models import Story, Task
from xp_tracker_app.forms import StoryForm, TaskForm
from xp_tracker_app.helper import delta_to_time
from django.utils import timezone
import datetime as dt


def index(request):
    contents = {}
    contents['stories'] = Story.objects.order_by('time_est')
    contents['tasks'] = Task.objects.order_by('iteration', 'time_est')

    spent_sum = dt.timedelta(0, 0)
    estimated_sum = dt.timedelta(0, 0)

    for task in contents['tasks']:
        if task.time_fin:
            spent_sum += task.time_fin - task.time_start
        estimated_sum += task.time_est - task.time_start

    contents['spent_sum'] = delta_to_time(spent_sum)
    contents['estimated_sum'] = delta_to_time(estimated_sum)

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
