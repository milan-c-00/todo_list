from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from tasks.models import Task


@login_required(login_url='login')
def all_tasks(request):
    # tasks = Task.objects.filter(user=request.user)
    tasks = request.user.task_set
    return render(request, 'tasks/all_tasks.html', {"tasks": tasks})


@login_required(login_url='login')
def create_task(request):
    if request.method == 'POST':
        if request.POST['description']:
            task = Task()
            task.description = request.POST['description']
            task.user = request.user
            task.save()
            return redirect('all_tasks')
        else:
            return render(request, 'tasks/create.html', {'error': 'Description is required field!'})
    else:
        return render(request, 'tasks/create.html')


@login_required(login_url='login')
def edit_task(request):
    pass


@login_required(login_url='login')
def done_task(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Task, pk=task_id)
        if task is not None:
            task.done = True
            task.save()
            return redirect('all_tasks')
        else:
            return render(request, 'tasks/all_tasks.html', {'error': 'Task not found!'})
    else:
        return render(request, 'tasks/all_tasks.html')


@login_required(login_url='login')
def delete_task(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Task, pk=task_id)
        if task is not None:
            task.delete()
            return redirect('all_tasks')
        else:
            return render(request, 'tasks/all_tasks.html', {'error': 'Task not found!'})
    else:
        return render(request, 'tasks/all_tasks.html')


