from django.forms import ModelForm
from django import forms

from .models import Phase, Task, Entity

class PhaseForm(ModelForm):
    class Meta:
        model   = Phase
        fields  = ['title', 'description', 'project']
        widgets = {'project': forms.HiddenInput()}
        
    def __init__(self, *args, **kwargs):
        super(PhaseForm, self).__init__(*args, **kwargs)
        self.fields['project'].initial = kwargs.get('project')
        
        
class TaskForm(ModelForm):
    class Meta:
        model   = Task
        fields  = ['title', 'description', 'phase']
        widgets = {'phase': forms.HiddenInput()}
        
    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['phase'].initial = kwargs.get('phase')
        
        
class EntityForm(ModelForm):
    class Meta:
        model   = Entity
        fields  = ['entity', 'description', 'type', 'service']
        widgets = {'service': forms.HiddenInput()}
        
    def __init__(self, *args, **kwargs):
        super(EntityForm, self).__init__(*args, **kwargs)
        self.fields['service'].initial = kwargs.get('service')
    
        
        