from django.shortcuts import render, redirect
from django.http import HttpResponse

from .sort import QuickSort
from .models import *
from .forms import *


# Create your views here.
def index(request, sort_type = 'id'):
    tasks =Task.objects.order_by(sort_type)# main_tasks

    form = TaskForm()
    context = {}
    context['sort_type'] = sort_type

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context['tasks'] = tasks
    context['form'] = form

    return render(request, 'Goals/list.html', context)#HttpResponse("To Do List")

def deleteTask(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == "POST":
        item.delete()
        return redirect('/')

    context = {'item': item}

    return render (request, 'Goals/delete.html', context)

def quickSort(request, sort_type):

    if request.method == "POST":

        return redirect('/')

    return render(request, 'Goals/quickSort.html')