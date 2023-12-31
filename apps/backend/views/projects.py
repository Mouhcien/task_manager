from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.http import Http404

from django.core.paginator import Paginator

from datetime import datetime, timezone

from ..models import Project

class ProjectListView(ListView):
    paginate_by     =   4
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
    projects    = Project.objects.filter(finished=False, ongoing=False).order_by('created_at')
    paginator   = Paginator(projects, 4) #Show 4 projects by row
    page_number = request.GET.get("page")
    page_obj    = paginator.get_page(page_number)
    context     = {'object_list': page_obj, 'tag': 'not-started', 'page_obj': page_obj}
    return render(request, 'projects/project_list.html', context)


def ProjectOnGoingList(request):
    projects    = Project.objects.filter(ongoing=True, finished=False).order_by('created_at')
    paginator   = Paginator(projects, 4) #Show 4 project by row
    page_number = request.GET.get("page")
    page_obj    = paginator.get_page(page_number)
    context     = {'object_list': page_obj, 'tag': 'ongoing', 'page_obj': page_obj}
    return render(request, 'projects/project_list.html', context)


def ProjectFinishedList(request):
    projects    = Project.objects.filter(finished=True).order_by('created_at')
    paginator   = Paginator(projects, 4) #Show 4 project by row
    page_number = request.GET.get("page")
    page_obj    = paginator.get_page(page_number)
    context     = {'object_list': page_obj, 'tag': 'finished', 'page_obj': page_obj}
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