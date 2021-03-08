from django.shortcuts import render, redirect, get_object_or_404

from To_do_list.forms import TaskForm
from To_do_list.models import Task, status_choices


# Create your views here.


def index_view(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, 'index.html', context)


def task_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task_view.html', context={'task': task})


def task_create_view(request):
    if request.method == 'GET':
        form = TaskForm()
        return render(request, 'task_create.html', context={'form': form})
    elif request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task = Task(
                title=form.cleaned_data.get('title'),
                status=form.cleaned_data.get('status'),
                date=form.cleaned_data.get('date'),
                add_info=form.cleaned_data.get('add_info')
            )
            task.save()
        else:
            return render(request, 'task_create.html', context={'form': form})
        return redirect('task_view', pk=task.id)


def task_update_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        form = TaskForm(initial={
            "title": task.title,
            "status": task.status,
            "date": task.date,
            "add_info": task.add_info,
        })
        return render(request, 'task_update.html', context={'form': form, "id": task.id})
    elif request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task.title = form.cleaned_data.get('title')
            task.status = form.cleaned_data.get('status')
            task.date = form.cleaned_data.get('date')
            task.add_info = form.cleaned_data.get('add_info')

            task.save()
        else:
            return render(request, 'task_update.html', context={'form': form, "id": task.id})
        return redirect('task_view', pk=task.id)


def task_delete_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        return render(request, 'task_delete.html', context={'task': task})
    elif request.method == 'POST':
        task.delete()
        return redirect('index')
