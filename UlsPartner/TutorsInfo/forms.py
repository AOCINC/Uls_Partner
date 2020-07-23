from django import forms
from .models import Tutors, Youtubers




class TutrosInfo_form(forms.ModelForm):
    class Meta:
        model = Tutors
        fields = '__all__'



class YoutubersInfo_form(forms.ModelForm):
    class Meta:
        model = Youtubers
        fields = '__all__'