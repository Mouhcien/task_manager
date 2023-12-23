from django.shortcuts import render

def index(request):
    context = {'message': 'This is the backend application for task manager'}
    return render(request=request, template_name='index.html', context=context)
