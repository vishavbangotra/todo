from django.shortcuts import render, redirect
from basicapp.models import *
from basicapp.forms import *

def home(request):
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        redirect('/')

    context = {
        'form': form, 'tasks': tasks
        }
    return render(request, 'home.html', context)

def update(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form': form,
    }
    return render(request, 'update.html', context)

def delete(request, pk):
    item = Task.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {
        "item":item
    }
    return render(request, 'delete.html', context)
