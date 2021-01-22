from django.shortcuts import render, redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.views.decorators.cache import cache_control
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import ensure_csrf_cookie
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile


# Create your views here.
# @login_required
# def profile(request):
#     if request.method == 'POST':
#         u_form = UserUpdateForm(request.POST, instance = request.user)
#         p_form = ProfileUpdateForm(request.POST,
#                                    request.FILES,
#                                    instance = request.user.profile)
#         if u_form.is_valid() and p_form.is_valid():
#             u_form.save()
#             p_form.save()
#             messages.success(request,f'Your Account Has Been Updated')
#             return redirect('profile')

#     else:
#         u_form = UserUpdateForm(instance = request.user)
#         p_form = ProfileUpdateForm(instance = request.user.profile)
#     # data  = Profile.objects.filter(user = request.user)
#     context ={
#         'u_form':u_form,
#         'p_form':p_form  
#         }
#     return render(request,'registration/profile.html',context)  



@login_required
@cache_control(no_cache=True,private=True, must_revalidate=True, no_store=True)
def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                messages.success(request,'you are  logged in')
                return redirect('/')
            else:
                messages.error(request,'invalid credentials')
                return redirect('login')
    else:
        return render(request,'registration/login.html')



@cache_control(no_cache=True,private=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('login')


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

@login_required
@cache_control(no_cache=True,private=True, must_revalidate=True, no_store=True)
def profile(request):
    template = 'registration/profile_sample.html'
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance = request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance = request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Your Account Has Been Updated')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance = request.user.profile)
    # data  = Profile.objects.filter(user = request.user)
    context ={
        'u_form':u_form,
        'p_form':p_form  
        }
    return render(request,template,context)