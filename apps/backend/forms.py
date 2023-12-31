from django.forms import ModelForm
from django import forms

from .models import Phase

class PhaseForm(ModelForm):
    class Meta:
        model   = Phase
        fields  = ['title', 'description', 'project']
        widgets = {'project': forms.HiddenInput()}
        
    def __init__(self, *args, **kwargs):
        super(PhaseForm, self).__init__(*args, **kwargs)
        self.fields['project'].initial = kwargs.get('project')
    
        
        