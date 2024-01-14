from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.core.paginator import Paginator

from ..models import Employee, Responsible

class EmployeeListView(ListView):
    paginate_by     =   8
    model           =   Employee
    template_name   =   'employees/employee_list.html'
    
class EmployeeCreateView(CreateView):
    model           =   Employee
    template_name   =   'employees/employee_create.html'
    fields          =   '__all__'
    success_url     =   reverse_lazy('employee-list')
    
class EmployeeUpdateView(UpdateView):
    model           =   Employee
    template_name   =   'employees/employee_create.html'
    fields          =   '__all__'
    success_url     =   reverse_lazy('employee-list')

class EmployeeDeleteView(DeleteView):
    model           =   Employee
    template_name   =   'employees/employees_delete.html'
    success_url     =   reverse_lazy('employee-list')
    
class EmployeeDetailView(DetailView):
    model           =   Employee
    template_name   =   'employees/employee_detail.html'
    
def employeeProjects(request, employee_id, tag):
    employee        = Employee.objects.get(id=employee_id)
    responsibles    = Responsible.objects.filter(employee_id=employee_id)
    paginator       = Paginator(responsibles, 4) #Show 4 entities by row
    page_number     = request.GET.get("page")
    page_obj        = paginator.get_page(page_number)
    context = {
        "object_list" : page_obj,
        "employee": employee,
        'page_obj': page_obj
    }
    if tag == 'projects-list':
        return render(request=request, template_name='employees/employee_projects.html', context=context)
    else:
        return render(request=request, template_name='employees/employee_tasks.html', context=context)