# main/forms.py
from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'item','link','category','limit','deadline',
        'body', 'image']
        labels = {
            'title':'제목',
            'category':'카테고리',
            'body':'본문',
            'item':'품목',
            'limit':'모집인원',
            'link':'링크',
            'deadline':'마감기한',
            'image':'사진'
        }


class PostSearchForm(forms.Form):
    category = forms.CharField(label='Category')
    search_word = forms.CharField(label='Search Word')
