from django.shortcuts import render, redirect



def home_view(request):
    template = 'Uls_PartnerApp/home.html'
    return render(request, template)


def Terms_Conditions(request):
    template_name = 'Uls_PartnerApp/terms_conditions.html'
    return render(request, template_name)


def privacy_policy(request):
    template_name = 'Uls_PartnerApp/privacy_policy.html'
    return render(request, template_name)


def Instructor_Conditions(request):
    template_name = 'Uls_PartnerApp/Instructor_Terms_Conditions.html'
    return render(request, template_name)


