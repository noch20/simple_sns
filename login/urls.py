from django.urls import path

from . import views

app_name = 'login'
urlpatterns = [
    path('', views.home, name='home'),
    path('logon', views.logon, name='logon'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
]