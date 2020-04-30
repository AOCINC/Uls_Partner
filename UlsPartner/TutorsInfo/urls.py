from django.urls import path
from TutorsInfo import views



urlpatterns = [
  path('Tutors-Info-Request',views.Tutors_InfoView, name = 'Tutors_Info_Request'), 
  path('success', views.Tutor_success, name = 'success'),

]