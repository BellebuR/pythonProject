from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def data_view(request):
    return HttpResponse('<h1>This is the Data Page</h1>')

def test_view(request):
    return HttpResponse('<h1>This is the Test Page</h1>')


def home_view(request):
    return HttpResponse("Главная страница")