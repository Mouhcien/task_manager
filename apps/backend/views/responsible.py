from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.shortcuts import redirect, render

from ..models import Responsible, Task
from ..forms import ResponsibleForm

class ResponsibleListView(ListView):
    paginate_by     =   4
    model           =   Responsible
    template_name   =   'responsibles/responsible_list.html'
    
class ResponsibleCreateView(CreateView):
    model           =   Responsible
    template_name   =   'responsibles/responsible_create.html'
    fields          =   '__all__'
    success_url     =   reverse_lazy('responsible-list')
    
class ResponsibleUpdateView(UpdateView):
    model           =   Responsible
    template_name   =   'responsibles/responsible_create.html'
    fields          =   '__all__'
    success_url     =   reverse_lazy('responsible-list')

class ResponsibleDeleteView(DeleteView):
    model           =   Responsible
    template_name   =   'responsibles/responsible_delete.html'
    success_url     =   reverse_lazy('responsible-list')
    
class ResponsibleDetailView(DetailView):
    model           =   Responsible
    template_name   =   'responsibles/responsible_detail.html'
    
def create_responsible_task(request, task_id):
    task  = Task.objects.get(id=task_id)
    if request.method == 'POST':
        responsibleForm   = ResponsibleForm(request.POST, {'task':task})
            
        if responsibleForm.is_valid():
            responsibleForm.save()
            return redirect('responsible-task-detail',task_id)
        else:
            context = {
                'form': responsibleForm,
            }
            return render(request=request, template_name='responsibles/responsible_create.html', context=context)
    else:
        responsibleForm   = ResponsibleForm({'task':task})
        context = {
            'form': responsibleForm,
        }
        return render(request=request, template_name='responsibles/responsible_create.html', context=context)
    

def responsible_task_detail(request, task_id):
    task            =   Task.objects.get(id=task_id)
    responsibles    =   Responsible.objects.filter(task_id=task_id)
    context = {
            'responsibles': responsibles,
            'task': task
        }
    return render(request=request, template_name='responsibles/responsible_detail.html', context=context)