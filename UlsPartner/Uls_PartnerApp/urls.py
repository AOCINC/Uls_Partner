from django.urls import path
from Uls_PartnerApp import views


urlpatterns = [
    path('',views.home_view, name = 'home'),
]
