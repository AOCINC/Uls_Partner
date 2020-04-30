from django import forms
from django.forms import Textarea
from .models import Projects



class ProjectsForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = '__all__' 
    
    
    Description = forms.CharField(widget = forms.Textarea(attrs ={ 
        'cols':200,
        'rows':5,
        'style':'width :100%',
        }))          