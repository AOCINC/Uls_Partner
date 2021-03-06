from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Tutors, Youtubers
from .forms import TutrosInfo_form,YoutubersInfo_form
from django.template.loader import get_template
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.template import Context
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.views.decorators.cache import never_cache






@login_required
def Tutor_success(request):
    template = 'TutorsInfo/Tutors_info_success.html'
    return render(request, template)

@cache_control(no_cache=True,private=True, must_revalidate=True, no_store=True)
@login_required
@never_cache
def Tutors_InfoView(request):
    if request.method == 'POST':
        Tutors_form = TutrosInfo_form(request.POST,instance = request.user.Tutors)
        if Tutors_form.is_valid():
            # sending Email from the requested tutors to ULS Team
            if request.user.is_authenticated:
                current_user       = request.user
                Education          = Tutors_form.cleaned_data['Education']
                certified_In       = Tutors_form.cleaned_data['Certified_In']
                email              = Tutors_form.cleaned_data['Email']
                phone              = Tutors_form.cleaned_data['Phone_Number']
                country            = Tutors_form.cleaned_data['Country']
                state              = Tutors_form.cleaned_data['State']
                Languages_Spoken   = Tutors_form.cleaned_data['Languages_Spoken']
                Tutor_subject      = Tutors_form.cleaned_data['Subjects']
                Expertise_subject  = Tutors_form.cleaned_data['Expertise_Subject']
                Year_Of_Experience = Tutors_form.cleaned_data['Year_Of_Experience']
                Teaching_Experience= Tutors_form.cleaned_data['Teaching_Experience']
                save_in_tutors = Tutors(
                                        user        = current_user,
                                        Education   = Education,
                                        Certified_In= Certified_In,
                                        Email       = email,
                                        Phone_Number = phone,
                                        Country     = country,
                                        State       = state,
                                        Languages_Spoken = Languages_Spoken,
                                        Subjects         = Tutor_subject,
                                        Expertise_Subject = Expertise_subject,
                                        Year_Of_Experience = Year_Of_Experience,
                                        Teaching_Experience = Teaching_Experience,
                                        )
                save_in_tutors.save() # saving the table 
                subject = 'A Request From Tutor'
                context ={
                          'User':current_user,
                          'email':email,
                          'phone':phone,
                          'country':country,
                          'state':state,
                          'Tutor_subject':Tutor_subject,
                          'Expertise_subject':Expertise_subject,
                         }
                from_email = 'email'
                to = ['itikpirfan@gmail.com','aocincpvtltd@gmail.com',]
                message = get_template('TutorsInfo/Tutors_email.html').render(context)
                msg = EmailMessage(subject, message, to=to,from_email = from_email)
                msg.content_subtype  = 'html'
                msg.send()        
                # mail sending to Partner/User . who dropped the request for his channel.......
                Tutor   = current_user
                Tutor_mail = email
                subject = 'Uls Team'
                context ={
                         'Tutor':Tutor,
                         }
                uls_email = 'aocincpvtltd@gmail.com'
                from_email = uls_email
                to = [Tutor_mail,]
                message = get_template('TutorsInfo/send_mail_to_partner.html').render(context)
                msg = EmailMessage(subject, message, to = to, from_email = from_email)
                msg.content_subtype = 'html'
                msg.send()
                # mail sending to partner/User ends here.
                return redirect('success')
    else:
        Tutors_form = TutrosInfo_form()
    context = {
               'Tutors_form':Tutors_form,
               
               }
    template = 'TutorsInfo/Tutors_Info_Request.html'
    return render(request, template, context)



def Tutors_Details_View(request):
    template  = 'TutorsInfo/Tutors_Details.html'
    name = request.user
    ed  = request.user.id
    data = Tutors.get_Tutor_Data_by_ids(name)
    # data = Tutors.objects.filter(user = ed)
    # print(Tutors.user.Education)
    print(data)
    for d in data:
        print(d.Education)
        print(d.Certified_In)
    context = {

    }
    return render(request,template,context)








@cache_control(no_cache=True,private=True, must_revalidate=True, no_store=True)
@login_required
@never_cache
def Youtubers_InfoView(request):
    if request.method == 'POST':
        Youtubers_form = YoutubersInfo_form(request.POST)
        if Youtubers_form.is_valid():
            Youtubers_form.save()
            # sending Email from the requested youtubers to ULS Team
            if request.user.is_authenticated:
                current_user       = request.user
                email              = Youtubers_form.cleaned_data['Email']
                phone              = Youtubers_form.cleaned_data['Phone_Number']
                country            = Youtubers_form.cleaned_data['Country']
                state              = Youtubers_form.cleaned_data['State']
                Youtube_Subject    = Youtubers_form.cleaned_data['Youtube_Subject']
                Youtube_Url        = Youtubers_form.cleaned_data['Youtube_Url']
                subject = 'A Request From Youtuber'
                context ={
                          'User':current_user,
                          'email':email,
                          'phone':phone,
                          'country':country,
                          'state':state,
                          'Youtube_Subject':Youtube_Subject,
                          'Youtube_Url':Youtube_Url,
                         }
                from_email = 'email'
                to = ['itikpirfan@gmail.com','aocincpvtltd@gmail.com',]
                message = get_template('TutorsInfo/Youtubers_email.html').render(context)
                msg = EmailMessage(subject, message, to=to,from_email = from_email)
                msg.content_subtype  = 'html'
                msg.send()        
                # mail sending to Partner/User . who dropped the request for his channel.......
                Tutor   = current_user
                Tutor_mail = email
                subject = 'Uls Team'
                context ={
                         'Tutor':Tutor,
                         }
                uls_email = 'aocincpvtltd@gmail.com'
                from_email = uls_email
                to = [Tutor_mail,]
                message = get_template('TutorsInfo/send_mail_to_partner.html').render(context)
                msg = EmailMessage(subject, message, to = to, from_email = from_email)
                msg.content_subtype = 'html'
                msg.send()
                # mail sending to partner/User ends here.
                return redirect('success')
    else:
        Youtubers_form = YoutubersInfo_form()
    context = {
               'Youtubers_form':Youtubers_form,
               }
    template = 'TutorsInfo/Youtubers_Info_Request.html'
    return render(request, template, context)

