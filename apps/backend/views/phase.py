
from django.shortcuts import render, redirect
from django.views.generic import  UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy

from ..models import Phase, Project
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
    phases = Phase.objects.filter(project_id=project_id)
    if (phases):
        context = {
            'error': False,
            'phases': phases,
            'project_id': project_id,
        }
    else:
        context = {
            'error': True,
            'message': 'There is no phases for this project',
            'project_id': project_id,
        }
    
    return render(request, 'phases/phase_list.html', context)

#Create new phases for a specific project
def create_new_phase(request, project_id):
    #my_project  = Project.objects.get(id=project_id)
    if request.method == 'POST':
        phaseForm               = PhaseForm()
        phaseForm.title         = request.POST.get('title')
        phaseForm.description   = request.POST.get('description')
        phaseForm.project_id    = project_id
        
        new_phase = phaseForm.cleaned_data
        print(new_phase)
            
        if phaseForm.is_valid():
            new_phase = phaseForm.cleaned_data
            print(new_phase)
            new_phase.save()
            return redirect('phase-list',project_id)
        else:
            context = {
                'form': phaseForm,
            }
            return render(request=request, template_name='phases/phase_create.html', context=context)
    else:
        phaseForm   = PhaseForm()
        context = {
            'form': phaseForm,
        }
        return render(request=request, template_name='phases/phase_create.html', context=context)
    
    
    


