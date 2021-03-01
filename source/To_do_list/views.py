from django.shortcuts import render
from To_do_list.models import Task,status_choices
# Create your views here.


def index_view(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, 'index.html', context)


def task_view(request):
    task_id = request.GET.get('id')
    task = Task.objects.get(pk=task_id)
    context = {'task': task}
    return render(request, 'task_view.html', context)


def task_create_view(request):
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
        return render(request, 'task_create.html', context)