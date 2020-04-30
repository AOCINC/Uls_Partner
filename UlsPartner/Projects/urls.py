from django.urls import path
from Projects import views



urlpatterns = [
  path('Projects-upload', views.Projects_View, name = 'Project_upload'),
]