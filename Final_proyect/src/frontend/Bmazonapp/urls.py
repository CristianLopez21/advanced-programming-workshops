from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='bmazon_home'),
    path('', views.login, name='bmazon_login')
]