from django import forms
from .models import Tutors, Youtubers




class TutrosInfo_form(forms.ModelForm):
    class Meta:
        model = Tutors
        fields = '__all__'
        # exclude = ('user',)
        widgets = {
            'Teaching_Experience': forms.Textarea(attrs={'rows':3, 'cols':3}),
        }



class YoutubersInfo_form(forms.ModelForm):
    class Meta:
        model = Youtubers
        fields = '__all__'