from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *
from .subClasses import *
from .sort import QuickSort

# Create your views here.

def index(request):
    tasks = Task.objects.all()#.order
    form = TaskForm()

    if request.method == "POST":
        #save a new form
        form = TaskForm(request.POST) #forgot .POST
        print(form.is_valid())
        if form.is_valid(): #returns true if no erros occurs 
            form.save() #saves form
        return redirect('/')

    context =  {'tasks': tasks, 'form': form}
    return render(request, "Goals/list.html", context)

def update_task(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm()

    if request.method == "POST":
        #updates the form of interest
        form = TaskForm(request.POST, instance=task)#forgot , instance = task
        if form.is_valid():
            form.save()
        return redirect('/')

    form.title = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new task...'}))
    context = {'task': task, 'form': form}
    return render(request, 'Goals/update_task.html', context)

def delete(request, pk):
    task = Task.objects.get(id=pk)

    ###     without having to create a .html    ###
    """ 
    if request.method == "GET":
        task.delete()
        return redirect('/')
    
    return redirect('/')
    """

    if request.method == "POST":
        task.delete()
        return redirect('/')
    
    context = {'task':task}
    return render(request, 'Goals/deleteWarning.html', context)

def mark_done(request, pk):
    task = Task.objects.get(id=pk)
    
    

    if request.method == "GET":
        task.complete = not task.complete
        task.save()
        return redirect('/')

    return redirect('/')

def sort_tasks(request):
    if request.method == "GET":
        tasks = Task.objects.all()
        tasks_0 = Task.objects.order_by('title')
        data_tasks = []

        for task in tasks_0:
            data_tasks.append(Task_data(task.title, task.complete, task.created))

        sorted_tasks = data_tasks#QuickSort(data_tasks)

        count = 0
        for task in tasks:
            
            task.title = sorted_tasks[count].title
            task.complete = sorted_tasks[count].complete
            task.created = sorted_tasks[count].created

            task.save()
            count +=1
        
        return redirect('/')

    return redirect('/')
    