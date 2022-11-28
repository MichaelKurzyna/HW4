from django.shortcuts import render, redirect
from .models import Todo
from .forms import TaskForm
from django.utils import timezone
# Create your views here.


def showtasks(request):
    if request.method == 'GET':
        search = request.GET.get('search') or ''
        tasks = Todo.objects.filter(task__contains=search)
        context = {'tasks': tasks}
        return render(request, 'index.html', context)
    tasks = Todo.objects.all()
    context = {'tasks': tasks}
    return render(request, 'index.html', context)


def add(request):
    form = TaskForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        return render(request, 'add.html')


def update(request, id):
    task = Todo.objects.get(id=id)
    form = TaskForm(request.POST or None, instance=task)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            task.updated_at = timezone.localtime()
            task.save()
            return redirect('index')
    return render(request, 'update.html', {'task': task})


def delete(request, id):
    task = Todo.objects.get(id=id)
    task.delete()
    return redirect('index')
