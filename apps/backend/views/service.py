from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy

from ..models import Service

class ServiceListView(ListView):
    model           =   Service
    template_name   =   'services/service_list.html'
    
class ServiceCreateView(CreateView):
    model           =   Service
    template_name   =   'services/service_create.html'
    fields          =   '__all__'
    success_url     =   reverse_lazy('service-list')
    
class ServiceUpdateView(UpdateView):
    model           =   Service
    template_name   =   'services/service_create.html'
    fields          =   '__all__'
    success_url     =   reverse_lazy('service-list')

class ServiceDeleteView(DeleteView):
    model           =   Service
    template_name   =   'services/service_delete.html'
    success_url     =   reverse_lazy('service-list')
    
class ServiceDetailView(DetailView):
    model           =   Service
    template_name   =   'services/service_detail.html'