from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('data/', views.data_view, name='data'),
    path('test/', views.test_view, name='test'),
    path('', views.home_view, name='home')
]