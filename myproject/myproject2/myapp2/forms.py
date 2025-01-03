from django import forms
from .models import News_post


class NewsPostForm(forms.ModelForm):
    class Meta:
        model = News_post
        fields = ['title', 'short_description', 'text']