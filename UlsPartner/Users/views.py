from django.shortcuts import render, redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.views.decorators.cache import cache_control
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import ensure_csrf_cookie
from .forms import UserRegisterForm


# Create your views here.

def SignUp(request):
    if request.method == 'POST':  
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,f'You Account has Been Created!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'registration/signup.html',{'form':form})

