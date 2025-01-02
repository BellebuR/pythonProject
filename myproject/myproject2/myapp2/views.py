from django.shortcuts import render

# Create your views here.
# myapp/views.py

from django.shortcuts import render

def home(request):
    return render(request, 'myapp2/home.html')

def news(request):
    return render(request, 'myapp2/news.html')

def creativity(request):
    return render(request, 'myapp2/creativity.html')

def misc(request):
    return render(request, 'myapp2/misc.html')