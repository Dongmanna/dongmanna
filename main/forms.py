# main/forms.py
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['category', 'title', 'body', 'item', 'limit', 'link', 'deadline']