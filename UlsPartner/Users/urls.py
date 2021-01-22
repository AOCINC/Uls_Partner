from django.urls import path
from Users import views


urlpatterns = [
    path('signup',views.SignUp, name = 'signup'),
    path('login',views.Login, name = 'login'),
    path('logout',views.logout,name='logout'),
    path('profile',views.profile, name = 'profile'),
    # path('test',views.profile, name = 'test'),
    

]
