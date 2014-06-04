import datetime as dt

from django.shortcuts import render, redirect
from django.utils import timezone

from xp_tracker_app.models import Story, Task, TaskFinishingHistory
from xp_tracker_app.forms import StoryForm, TaskForm
from xp_tracker_app.helper import delta_to_time

def index(request):
    """ View for rendering index page. """

    # creating conents dictionary, for storing all objects and values, 
    # that will be  passes to template
    contents = {}
    contents['stories'] = Story.objects.order_by('time_est')

    # ordering tasks, to be able to see tasks in iteration order, 
    # and within the iteration in closes deadline (time_est) order.
    contents['tasks'] = Task.objects.order_by('iteration', 'time_est')

    spent_sum = dt.timedelta(0, 0) # sum of spent work hours on tasks
    estimated_sum = dt.timedelta(0, 0) # sum of estimated work hours on tasks

    for task in contents['tasks']:
        if task.time_fin:
            spent_sum += task.time_fin - task.time_start
        estimated_sum += task.time_est - task.time_start

    # converting dt.timedelta values to "d:h:m:s" format
    contents['spent_sum'] = delta_to_time(spent_sum)
    contents['estimated_sum'] = delta_to_time(estimated_sum)

    return render(request, 'index.html', contents)

def new_story(request):
    """ View to render new story form """
    form = StoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'new_story.html', {'form':form})

def new_task(request):
    """ View to render new story form """
    form = TaskForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'new_task.html', {'form':form})

def task_finished(request, task_pk):
    """ 
    View for saving task finishing/updating time.
    For Task object time_fin is saved (and overwritten) as now() time,
    the same time value is stored in related table - TaskFinishingHistory.
    This table stores multiple task finishing/updating time values for the Task.
    """
    task = Task.objects.get(pk=task_pk)
    time_fin = timezone.now()
    TaskFinishingHistory.objects.create(task=task, time_fin=time_fin)
    task.time_fin = time_fin
    task.save()
    return redirect('index')
