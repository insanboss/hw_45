from django.shortcuts import render, redirect
from To_do_list.models import Task, status_choices
from django.http import Http404
from django.urls import reverse
# Create your views here.


def index_view(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, 'index.html', context)


def task_view(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        raise Http404
    return render(request, 'task_view.html', context={'task': task})


def task_create_view(request, *args, **kwargs):
    if request.method == 'GET':
        return render(request, 'task_create.html', context={'status': status_choices})
    elif request.method == 'POST':
        title = request.POST.get('title')
        status = request.POST.get('status')
        date = request.POST.get('date')
        task = Task.objects.create(title=title, status=status, date=date)
        context = {
            'task': task
        }
        return redirect('task_add', pk=task.id)
