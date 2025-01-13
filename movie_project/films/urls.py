from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('add/', views.add_film, name='add_film'),
    path('list/', views.film_list, name='film_list'),
]