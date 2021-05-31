from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('login', views.log, name='log'),
    path('logout', views.logoutuser, name='logout'),
    path('create', views.create, name='create'),
    path('<int:adId>', views.detail, name='detail'),
    path('my', views.my, name='my'),
    path('my/<int:adId>', views.edit, name='edit')
]
