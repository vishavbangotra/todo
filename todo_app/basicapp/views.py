from django.shortcuts import render, redirect
from .models import Todo
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.views.generic import (TemplateView, ListView, DetailView,)
from basicapp.forms import TaskForm
# Create your views here.
def index(request):
    todos  = Todo.objects.all().order_by('date_added')
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'index.html', {'todos':todos, 'form':form})

def update(request, pk):
    updatetask = Todo.objects.get(id=pk)
    form = TaskForm(instance=updatetask)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=updatetask)
        if form.is_valid():
            form.save()
            return redirect(index)
    return render(request, 'update.html', {'form': form})

def delete(request, pk):
    deletetask = Todo.objects.get(id=pk)
    if request.method == 'POST':
        deletetask.delete()
        return redirect(index)
    return render(request, 'delete.html', {'name': deletetask.title})
