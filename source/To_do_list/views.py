from django.shortcuts import render, redirect, get_object_or_404
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
        return render(request, 'task_create.html', context={'status': status_choices})
    elif request.method == 'POST':
        title = request.POST.get('title')
        status = request.POST.get('status')
        date = request.POST.get('date')
        if not date:
            date = None
        task = Task.objects.create(title=title, status=status, date=date)

        return redirect('task_view', pk=task.id)
