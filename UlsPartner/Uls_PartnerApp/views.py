from django.shortcuts import render, redirect



def home_view(request):

    template = 'Uls_PartnerApp/home.html'
    return render(request, template)

