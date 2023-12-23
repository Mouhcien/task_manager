from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.shortcuts import render

from ..models import Project

class ProjectListView(ListView):
    model           =   Project
    template_name   =   'projects/project_list.html'
    
class ProjectCreateView(CreateView):
    model           =   Project
    template_name   =   'projects/project_create.html'
    fields          =   '__all__'
    success_url     =   reverse_lazy('project-list')
    
class ProjectUpdateView(UpdateView):
    model           =   Project
    template_name   =   'projects/project_create.html'
    fields          =   '__all__'
    success_url     =   reverse_lazy('project-list')

class ProjectDeleteView(DeleteView):
    model           =   Project
    template_name   =   'projects/project_delete.html'
    success_url     =   reverse_lazy('project-list')
    
class ProjectDetailView(DetailView):
    model           =   Project
    template_name   =   'projects/project_detail.html'
    
def ProjectOnGoingList(request):
    projects = Project.objects.filter(ongoing=True)
    context = {'object_list': projects}
    return render(request, 'projects/project_list.html', context)

def ProjectFinishedList(request):
    projects = Project.objects.filter(finished=True)
    context = {'object_list': projects}
    return render(request, 'projects/project_list.html', context)