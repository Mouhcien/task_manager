
from django.shortcuts import render
from django.views.generic import  CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy

from ..models import Phase

class PhaseCreateView(CreateView):
    model           =   Phase
    template_name   =   'phases/phase_create.html'
    fields          =   '__all__'
    success_url     =   reverse_lazy('project-list')

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
    phases = Phase.objects.filter(project_id=project_id)
    if (phases):
        context = {
            'error': False,
            'phases': phases
        }
    else:
        context = {
            'error': True,
            'message': 'There is no phases for this project'
        }
    
    return render(request, 'phases/phase_list.html', context)


