from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.http import Http404

from datetime import datetime, timezone

from ..models import Project

class ProjectListView(ListView):
    model           =   Project
    template_name   =   'projects/project_list.html'
    
    
class ProjectCreateView(CreateView):
    model           =   Project
    template_name   =   'projects/project_create.html'
    fields          =   ['title', 'description']
    success_url     =   reverse_lazy('project-list')
    
    
class ProjectUpdateView(UpdateView):
    model           =   Project
    template_name   =   'projects/project_create.html'
    fields          =   ['title', 'description']
    success_url     =   reverse_lazy('project-list')


class ProjectDeleteView(DeleteView):
    model           =   Project
    template_name   =   'projects/project_delete.html'
    success_url     =   reverse_lazy('project-list')
    
    
class ProjectDetailView(DetailView):
    model           =   Project
    template_name   =   'projects/project_detail.html'


def ProjectNotStartedList(request):
    projects = Project.objects.filter(finished=False, ongoing=False)
    context = {'object_list': projects, 'tag': 'not-started', 'with_header': True}
    return render(request, 'projects/project_list.html', context)


def ProjectOnGoingList(request):
    projects = Project.objects.filter(ongoing=True, finished=False)
    context = {'object_list': projects, 'tag': 'ongoing', 'with_header': True}
    return render(request, 'projects/project_list.html', context)


def ProjectFinishedList(request):
    projects = Project.objects.filter(finished=True)
    context = {'object_list': projects, 'tag': 'finished', 'with_header': True}
    return render(request, 'projects/project_list.html', context)

def StartProject(request, pk):
    project     = Project.objects.get(id=pk)
    if project:
        project.ongoing     = True
        project.started_at  =  datetime.now(timezone.utc)
        project.updated_at  =  datetime.now(timezone.utc)
        project.save()
        context = {'object': project, 'message': 'Project has been started successfuly'}
    else:
        raise Http404("No such project")
    
    return render(request, 'projects/project_detail.html', context)

def TerminateProject(request, pk):
    project     = Project.objects.get(id=pk)
    if project:
        project.finished        = True
        project.finished_at     =  datetime.now(timezone.utc)
        project.updated_at      =  datetime.now(timezone.utc)
        project.save()
        context = {'object': project, 'message': 'Project has been started successfuly'}
    else:
        raise Http404("No such project")
    
    return render(request, 'projects/project_detail.html', context)