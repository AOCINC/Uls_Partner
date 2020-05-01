from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.views.decorators.cache import never_cache
from .models import Projects
from .forms import ProjectsForm
from django.template.loader import get_template
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.template import Context





@login_required
def Project_Success(request):
    template = 'Projects/Projects_info_success.html'
    return render(request, template)




@cache_control(no_cache=True,private=True, must_revalidate=True, no_store=True)
@login_required
def Projects_View(request):
    if request.method == 'POST':
        Form = ProjectsForm(request.POST)
        if Form.is_valid():
            Form.save()
            # sending mail to uls team 
            if request.user.is_authenticated:
                current_user       = request.user
                email              = current_user.email
                phone              = current_user.profile.Phone_Number
                title              = Form.cleaned_data['Title']
                Description        = Form.cleaned_data['Description']
                location           = Form.cleaned_data['Location']
                duration           = Form.cleaned_data['Duration']
                In                 = Form.cleaned_data['In']
                subject = 'A Uls Partner Posted New Project Requirement'
                context ={
                          'User':current_user,
                          'email':email,
                          'phone':phone,
                          'title':title,
                          'Description':Description,
                          'location':location,
                          'duration':duration,
                          'In':In,                  
                          }
                from_email = 'email'
                to = ['itikpirfan@gmail.com','aocincpvtltd@gmail.com',]
                message = get_template('Projects/Projects_Request_email.html').render(context)
                msg = EmailMessage(subject, message, to=to,from_email = from_email)
                msg.content_subtype  = 'html'
                msg.send()
                # mail to uls team ended
                # sending mail to uls partner that mail request has submitted
                Uls_Partner   = current_user
                Partner_mail =  email
                subject = 'Uls Management Team'
                context ={
                         'Uls_Partner':Uls_Partner,
                         }
                uls_email = 'aocincpvtltd@gmail.com'
                from_email = uls_email
                to = [Partner_mail,]
                message = get_template('Projects/send_mail_to_partner.html').render(context)
                msg = EmailMessage(subject, message, to = to, from_email = from_email)
                msg.content_subtype = 'html'
                msg.send()
                # sending mail to uls partner ends here
            return redirect('success')

    else:
        Form = ProjectsForm()
    context = {
               'Form':Form,
    }
    template = 'Projects/Project_Upload.html'
    return render(request, template, context)