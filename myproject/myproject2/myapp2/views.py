from django.shortcuts import render

# Create your views here.
# myapp/views.py

from .models import News_post

from django.shortcuts import render

from django.shortcuts import render, redirect
from .forms import NewsPostForm

def home(request):
    return render(request, 'myapp2/home.html')

def news(request):
    news = News_post.objects.all()
    return render(request, 'myapp2/news.html', {'news': news})

def creativity(request):
    return render(request, 'myapp2/creativity.html')

def misc(request):
    return render(request, 'myapp2/misc.html')

def create_news_post(request):
    if request.method == 'POST':
        form = NewsPostForm(request.POST)
        if form.is_valid():
            news_post = form.save(commit=False)
            news_post.author = request.user
            news_post.save()
            return redirect('news_list')
    else:
        form = NewsPostForm()
    return render(request, 'news/create_news_post.html', {'form': form})




