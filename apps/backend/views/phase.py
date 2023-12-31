
from django.shortcuts import render, redirect
from django.views.generic import  UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy

from ..models import Phase, Project, Task
from ..forms import PhaseForm

class PhaseUpdateView(UpdateView):
    model           =   Phase
    template_name   =   'phases/phase_create.html'
    fields          =   '__all__'
    success_url     =   reverse_lazy('project-list')

class PhaseDeleteView(DeleteView):
    model           =   Phase
    template_name   =   'phases/phase_delete.html'
    success_url     =   reverse_lazy('project-list')

class PhaseDetailView(DetailView):
    model           =   Phase
    template_name   =   'phases/phase_detail.html'

#Get all the phases of a project
def phase_list(request, project_id):
    phases  = Phase.objects.filter(project_id=project_id)
    project = Project.objects.get(id=project_id)
    if (phases):
        context = {
            'error': False,
            'phases': phases,
            'project_id': project_id,
            'project': project,
        }
    else:
        context = {
            'error': True,
            'message': 'There is no phases for this project',
            'project_id': project_id,
            'project': project,
        }
    
    return render(request, 'phases/phase_list.html', context)

#Create new phases for a specific project
def create_new_phase(request, project_id):
    project  = Project.objects.get(id=project_id)
    if request.method == 'POST':
        phaseForm   = PhaseForm(request.POST, {'project':project})
            
        if phaseForm.is_valid():
            phaseForm.save()
            return redirect('phase-list',project_id)
        else:
            context = {
                'form': phaseForm,
            }
            return render(request=request, template_name='phases/phase_create.html', context=context)
    else:
        phaseForm   = PhaseForm({'project':project})
        context = {
            'form': phaseForm,
        }
        return render(request=request, template_name='phases/phase_create.html', context=context)
    
def phase_detail(request, pk):
    phase = Phase.objects.get(id=pk)
    if phase:
        #Get all the tasks
        tasks = Task.objects.filter(phase=phase)
        if tasks:
            context = {
                'object': phase,
                'tasks': tasks,
                'error': False,
            } 
        else:
            context = {
                'object': phase,
                'message_task': 'There is no tasks in this phase',
                'error': True,
            } 
    else:
        context = {
            'error': True,
            'message': 'not found'
        }
    
    return render(request=request, template_name='phases/phase_detail.html', context=context)
    


