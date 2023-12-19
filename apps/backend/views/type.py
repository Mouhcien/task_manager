from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy

from ..models import Entity_Type

class Entity_TypeListView(ListView):
    model           =   Entity_Type
    template_name   =   'entity_types/entity_types_list.html'
    
class Entity_TypeCreateView(CreateView):
    model           =   Entity_Type
    template_name   =   'entity_types/entity_types_create.html'
    fields          =   '__all__'
    success_url     =   reverse_lazy('entity-type-list')
    
class Entity_TypeUpdateView(UpdateView):
    model           =   Entity_Type
    template_name   =   'entity_types/entity_types_create.html'
    fields          =   '__all__'
    success_url     =   reverse_lazy('entity-type-list')

class Entity_TypeDeleteView(DeleteView):
    model           =   Entity_Type
    template_name   =   'entity_types/entity_types_delete.html'
    success_url     =   reverse_lazy('entity-type-list')
    
class Entity_TypeDetailView(DetailView):
    model           =   Entity_Type
    template_name   =   'entity_types/entity_types_detail.html'