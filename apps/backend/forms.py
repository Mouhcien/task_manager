from django.forms import ModelForm
from django import forms

from .models import Phase

class PhaseForm(forms.Form):
    title       = forms.CharField(max_length=150, required=True)
    description = forms.CharField(widget=forms.Textarea, required=True)
    project_id  = forms.IntegerField(widget = forms.HiddenInput(), required=True)
    
        
        