from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *

schedules = []
# Create your views here.


def index(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == "POST":
        
        form = TaskForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            task = Task(title=title)
            task.save()
        return redirect('/')

    context = {'tasks':tasks, 'form':form}
    return render(request, 'Goals/index.html', context)
  

def task_list(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == "POST":
        
        form = TaskForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
        return redirect('list')

    context = {'tasks':tasks, 'form':form}

    return render(request, 'Goals/list.html', context)

def delete_task(request, pk):
    task = Task.objects.get(id=pk)

    if request.method == "POST":
        task.delete()
        return redirect('list')
    
    return render(request, 'Goals/delete_task.html', {'task' :task})

def edit_task(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm()

    if request.method == "POST":
        task = TaskForm(request.POST, instance = task)
        task.save()
        return redirect('list')
    
    context = {'task':task, 'form':form}
    return render(request, 'Goals/edit_task.html', context)

def sort(request):
    tasks = Task.objects.all()
    sorted_task = Task.objects.order_by('priority', 'title')
    data_tasks = []
    
    for task in sorted_task:
        data_tasks.append(task_data(task.title, task.done, task.created_at, task.priority, task.parent_list_id))
    
    count = 0
    for task in tasks:
        task.title = data_tasks[count].title
        task.done = data_tasks[count].done
        task.created_at = data_tasks[count].created_at
        task.parent_list_id = data_tasks[count].parent_list_id
        count+=1
        task.save()
    return redirect('list')

def mark_done(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == "GET":
        task.done = not task.done
        task.save()
        return redirect('list')
    return redirect('list')



## classes
class task_data:
    def __init__(self, title, done, created_at, priority, parent_list_id):
        self.title = title
        self.done = done
        self.created_at = created_at
        self.priority = priority
        self.parent_list_id = parent_list_id
