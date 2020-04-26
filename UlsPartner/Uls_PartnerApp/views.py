from django.shortcuts import render


def home_view(request):

    template = 'Uls_PartnerApp/home.html'
    return render(request, template)