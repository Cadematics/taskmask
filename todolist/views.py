from django.shortcuts import render, redirect
from todolist.models import TaskList
from todolist.form import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    context = {
        'index_text':"Welcome to the index page"
    }
    return render(request, 'index.html', context)

@login_required
def todolist(request):
    if request.method=='POST':
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save(commit=False).manage = request.user
            form.save()
            messages.success(request, 'New Task Added!')
        return redirect('todolist_page')
    else:
        all_tasks = TaskList.objects.filter(manage=request.user)
        paginator = Paginator(all_tasks, 5)
        page = request.GET.get('pg')
        all_tasks = paginator.get_page(page)
        context = {
            'all_tasks': all_tasks,
            'request':dir(request)
        }
        return render(request, 'todolist.html', context)
@login_required
def contact(request):
    context = {
        'contact_text': 'welcome to the contact page'
    }
    return render(request, 'contact.html', context)

def about(request):
    context = {
        'about_text': 'Welcome to the about page'
    }
    return render(request, 'about.html', context)

@login_required
def new_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
        return redirect ('todolist_page')
    else:
        return render(request, 'new_task.html', {})

@login_required
def delete_task(request, task_id):
    task = TaskList.objects.get(pk = task_id)
    if task.manage == request.user:
        task.delete()
    else:
        messages.error(request, 'You are not allowed!' ) 
    return redirect('todolist_page')

@login_required
def completed_task(request, task_id):
    task = TaskList.objects.get(pk = task_id)
    if task.manage == request.user:
        task.done = True
        task.save()
    else:
        messages.error(request, 'Operation not allowed')
    return redirect('todolist_page')
@login_required
def pending_task(request, task_id):
    task = TaskList.objects.get(pk = task_id)
    if task.manage == request.user:
        task.done = False
        task.save()
    else:
        messages.error(request, 'Operation not allowed')
    return redirect('todolist_page')

@login_required
def edit_task(request, task_id):
    if request.method=='POST':
        task = TaskList.objects.get(pk=task_id)
        if task.manage == request.user:
            form = TaskForm(request.POST or None, instance=task )
            if form.is_valid():
                form.save()
            messages.success(request, 'Task Edited!')
        else:
            messages.error(request, 'Operation not allowed')
        
    else:
        task_obj = TaskList.objects.get(pk=task_id)
        if task_obj.manage == request.user:
            context = {
                'task_obj': task_obj
            }
            return render(request, 'edit_task.html', context)
        else:
            messages.error(request, 'Operation not allowed')
    return redirect('todolist_page') 