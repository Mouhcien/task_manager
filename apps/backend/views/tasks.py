
from django.shortcuts import render, redirect
from django.views.generic import  UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.http import Http404

from datetime import datetime, timezone

from ..models import Task, Phase
from ..forms import TaskForm

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
            'tasks': tasks,
            'phase_id': phase_id
        }
    else:
        context = {
            'error': True,
            'message': 'There is no tasks for this phase',
            'phase_id': phase_id
        }
    
    return render(request, 'tasks/task_list.html', context)

#Create new tasks for a specific phase
def create_new_task(request, phase_id):
    phase  = Phase.objects.get(id=phase_id)
    if request.method == 'POST':
        taskForm   = TaskForm(request.POST, {'phase':phase})
        if taskForm.is_valid():
            taskForm.save()
            return redirect('task-list', phase_id)
        else:
            context = {
                'form': taskForm,
            }
            return render(request=request, template_name='tasks/task_create.html', context=context)
    else:
        taskForm   = TaskForm({'phase':phase})
        context = {
            'form': taskForm,
        }
        return render(request=request, template_name='tasks/task_create.html', context=context)

def startTask(request, pk):
    task     = Task.objects.get(id=pk)
    if task:
        task.ongoing     = True
        task.started_at  =  datetime.now(timezone.utc)
        task.updated_at  =  datetime.now(timezone.utc)
        task.save()
    else:
        raise Http404("No such task")
    
    return redirect('task-list', task.phase.id)

def terminateTask(request, pk):
    task     = Task.objects.get(id=pk)
    if task:
        task.finished        = True
        task.finished_at     =  datetime.now(timezone.utc)
        task.updated_at      =  datetime.now(timezone.utc)
        task.save()
    else:
        raise Http404("No such task")
    
    return redirect('task-list', task.phase.id)
