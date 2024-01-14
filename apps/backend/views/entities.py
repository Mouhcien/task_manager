from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from ..models import Entity, Service
from ..forms import EntityForm

class EntityListView(ListView):
    paginate_by     =   4
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
    
#Get all entities by service_id 
def enitities_list(request, service_id):
    entities    = Entity.objects.filter(service_id=service_id)
    paginator   = Paginator(entities, 4) #Show 4 entities by row
    page_number = request.GET.get("page")
    page_obj    = paginator.get_page(page_number)
    context = {
        "object_list" : page_obj,
        "service_id": service_id,
        'page_obj': page_obj
    }
    return render(request=request, template_name='entities/entity_list.html', context=context)


def create_new_entity(request, service_id):
    service  = Service.objects.get(id=service_id)
    if request.method == 'POST':
        entityForm   = EntityForm(request.POST, {'service':service})
            
        if entityForm.is_valid():
            entityForm.save()
            return redirect('service-entities-list',service_id)
        else:
            context = {
                'form': entityForm,
            }
            return render(request=request, template_name='entities/entity_create.html', context=context)
    else:
        entityForm   = EntityForm({'service':service})
        context = {
            'form': entityForm,
        }
        return render(request=request, template_name='entities/entity_create.html', context=context)