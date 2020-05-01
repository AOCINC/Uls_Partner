from django.urls import path
from Projects import views



urlpatterns = [
  path('Projects-upload', views.Projects_View, name = 'Project_upload'),
  path('success', views.Project_Success, name = 'sucess'),
]