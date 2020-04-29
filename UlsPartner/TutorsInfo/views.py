from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Tutors 
from .forms import TutrosInfo_form
from django.template.loader import get_template
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.template import Context
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.views.decorators.cache import never_cache







def Tutor_success(request):
    template = 'TutorsInfo/Tutors_info_success.html'
    return render(request, template)

@cache_control(no_cache=True,private=True, must_revalidate=True, no_store=True)
@login_required
@never_cache
def Tutors_InfoView(request):
    if request.method == 'POST':
        Tutors_form = TutrosInfo_form(request.POST)
        if Tutors_form.is_valid():
            Tutors_form.save()
            # sending Email from the requested tutors
            if request.user.is_authenticated:
                current_user       = request.user
                email              = Tutors_form.cleaned_data['Email']
                phone              = Tutors_form.cleaned_data['Phone_Number']
                country            = Tutors_form.cleaned_data['Country']
                state              = Tutors_form.cleaned_data['State']
                Tutor_subject      = Tutors_form.cleaned_data['Youtube_Subject']
                
                ytube_Url    = Tutors_form.cleaned_data['Youtube_Url']
                subject = 'A Request From Tutor'
                context ={
                          'User':current_user,
                          'email':email,
                          'phone':phone,
                          'country':country,
                          'state':state,
                          'Tutor_subject':Tutor_subject,
                          'ytube_Url':ytube_Url,
                         }
                from_email = 'email'
                to = ['itikpirfan@gmail.com','aocincpvtltd@gmail.com',]
                message = get_template('TutorsInfo/Tutors_email.html').render(context)
                msg = EmailMessage(subject, message, to=to,from_email = from_email)
                msg.content_subtype  = 'html'
                msg.send()       
                return redirect('success')
    else:
        Tutors_form = TutrosInfo_form()
    context = {
               'Tutors_form':Tutors_form,
               }
    template = 'TutorsInfo/Tutors_Info_Request.html'
    return render(request, template, context)
