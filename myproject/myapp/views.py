from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def data_view(request):
    return render(request, template_name='myapp/data.html')

def test_view(request):
    return render(request, template_name='myapp/test.html')


def home_view(request):
    return render(request, template_name='myapp/home.html', context={'caption': 'FamalyVin'})