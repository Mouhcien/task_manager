from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from ..models import Project

class ProjectListView(ListView):
    model           =   Project
    template_name   =   'projects/project_list.html'
    
class ProjectCreateView(CreateView):
    model           =   Project
    template_name   =   'projects/project_create.html'
    fields          =   '__all__'
    
class ProjectUpdateView(UpdateView):
    model           =   Project
    template_name   =   'projects/project_create.html'
    fields          =   '__all__'

class ProjectDeleteView(DeleteView):
    model           =   Project
    template_name   =   'projects/project_delete.html'