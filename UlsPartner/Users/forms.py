from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            match = User.objects.get(email = email)
        except:
            return self.cleaned_data['email']
        raise forms.ValidationError('Email Is Already Exists!')



class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta(object):
        model = User
        fields = ['username','email']
                  

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image',
                  'Company',
                  'Adhar_Number',
                  'Phone_Number',
                  'GST_Number',            
                  'Pan_Number',
                  'CIN_Number',
                  'Company_Postal_Address',
                  'Bank_Account_Number',
                  'IFSC',
                  'Branch',
                  
                  ]
