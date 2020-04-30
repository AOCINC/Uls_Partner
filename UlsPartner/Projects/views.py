from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.views.decorators.cache import never_cache
from .models import Projects
from .forms import ProjectsForm


@cache_control(no_cache=True,private=True, must_revalidate=True, no_store=True)
@login_required
def Projects_View(request):
    if request.method == 'POST':
        Form = ProjectsForm(request.POST)
        if Form.is_valid():
            Form.save()
            return redirect('home')

    else:
        Form = ProjectsForm()
    context = {
               'Form':Form,
    }
    template = 'Projects/Project_Upload.html'
    return render(request, template, context)