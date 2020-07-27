from django.urls import path
from Uls_PartnerApp import views


urlpatterns = [
    path('',views.home_view, name = 'home'),
    path('terms-conditions', views.Terms_Conditions, name = 'terms_conditions'),
    path('privacy-policy', views.privacy_policy, name = 'pravacy_policy')

]
