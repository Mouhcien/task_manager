from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy

from ..models import Employee

class EmployeeListView(ListView):
    paginate_by     =   4
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