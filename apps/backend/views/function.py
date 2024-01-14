from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy

from ..models import Function

class FunctionListView(ListView):
    paginate_by     =   4
    model           =   Function
    template_name   =   'functions/function_list.html'
    
class FunctionCreateView(CreateView):
    model           =   Function
    template_name   =   'functions/function_create.html'
    fields          =   '__all__'
    success_url     =   reverse_lazy('function-list')
    
class FunctionUpdateView(UpdateView):
    model           =   Function
    template_name   =   'functions/function_create.html'
    fields          =   '__all__'
    success_url     =   reverse_lazy('function-list')

class FunctionDeleteView(DeleteView):
    model           =   Function
    template_name   =   'functions/functions_delete.html'
    success_url     =   reverse_lazy('function-list')
    
class FunctionDetailView(DetailView):
    model           =   Function
    template_name   =   'functions/function_detail.html'