# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('news/', views.news, name='news'),
    path('creativity/', views.creativity, name='creativity'),
    path('misc/', views.misc, name='misc'),
]