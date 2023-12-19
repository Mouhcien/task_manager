
from django.shortcuts import render
from django.views.generic import  CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy

from ..models import Task

class TaskCreateView(CreateView):
    model           =   Task
    template_name   =   'tasks/task_create.html'
    fields          =   '__all__'
    success_url     =   reverse_lazy('project-list')

class TaskUpdateView(UpdateView):
    model           =   Task
    template_name   =   'tasks/task_create.html'
    fields          =   '__all__'
    success_url     =   reverse_lazy('project-list')

class TaskDeleteView(DeleteView):
    model           =   Task
    template_name   =   'tasks/task_delete.html'
    success_url     =   reverse_lazy('project-list')

class TaskDetailView(DetailView):
    model           =   Task
    template_name   =   'tasks/task_detail.html'

#Get all the tasks of a phase of a project
def task_list(request, phase_id):
    tasks = Task.objects.filter(phase_id=phase_id)
    if (tasks):
        context = {
            'error': False,
            'tasks': tasks
        }
    else:
        context = {
            'error': True,
            'message': 'There is no tasks for this phase'
        }
    
    return render(request, 'tasks/task_list.html', context)


