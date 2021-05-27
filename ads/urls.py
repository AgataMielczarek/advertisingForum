from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('login', views.log, name='log'),
    path('logout', views.logoutuser, name='logout'),
]
