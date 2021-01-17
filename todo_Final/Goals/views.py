from django.forms.widgets import TextInput
from django.shortcuts import render, redirect

from.models import *
from .forms import *

# Create your views here.
def index(request):

    tasks = Task.objects.all()
    #form = TaskForm()


    context = {'tasks':tasks}
    
    return render(request, "Goals/index.html", context)

def view_list(request):
    search_query = request.GET.get('search', '')

    if search_query:
        tasks = Task.objects.filter(title__icontains = search_query)
    else:

        tasks = Task.objects.all()
    form = TaskForm()



    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('list')




    context = {'tasks':tasks, 'form':form}
    
    return render(request, "Goals/list.html", context)

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
    sorted_task = Task.objects.order_by('done','title')
    data_tasks = []
    
    for task in sorted_task:
        data_tasks.append(task_data(task.title, task.done, task.created_at))
    
    count = 0
    for task in tasks:
        task.title = data_tasks[count].title
        task.done = data_tasks[count].done
        task.created_at = data_tasks[count].created_at
        
        count+=1
        task.save()
    return redirect('list')

def mark_done(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == "GET":
        print(task.done)
        task.done = not task.done
        task.save()
        return redirect('list')
    return redirect('list')



## classes
class task_data:
    def __init__(self, title, done, created_at):
        self.title = title
        self.done = done
        self.created_at = created_at

