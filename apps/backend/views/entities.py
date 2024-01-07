from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy

from ..models import Entity

class EntityListView(ListView):
    model           =   Entity
    template_name   =   'entities/entity_list.html'
    
class EntityCreateView(CreateView):
    model           =   Entity
    template_name   =   'entities/entity_create.html'
    fields          =   '__all__'
    success_url     =   reverse_lazy('entity-type-list')
    
class EntityUpdateView(UpdateView):
    model           =   Entity
    template_name   =   'entities/entity_create.html'
    fields          =   '__all__'
    success_url     =   reverse_lazy('entity-type-list')

class EntityDeleteView(DeleteView):
    model           =   Entity
    template_name   =   'entities/entity_delete.html'
    success_url     =   reverse_lazy('entity-type-list')
    
class EntityDetailView(DetailView):
    model           =   Entity
    template_name   =   'entities/entity_detail.html'