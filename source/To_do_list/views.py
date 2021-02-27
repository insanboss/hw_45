from django.shortcuts import render
from To_do_list.models import Task
# Create your views here.


def index_view(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, 'index.html', context)

def task_view(request):
    task_id = request.GET.get('pk')
    task = Task.objects.get(pk=task_id)
    context = {'task': task}
    return render(request, 'task_view.html', context)