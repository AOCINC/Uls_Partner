from django import forms
from .models import Tutors




class TutrosInfo_form(forms.ModelForm):
    class Meta:
        model = Tutors
        fields = '__all__'