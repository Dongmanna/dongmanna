# main/forms.py
from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post

        fields = [ 'category','title', 'body', 'item', 'limit', 'link', 'deadline','image']




class PostSearchForm(forms.Form):
    category = forms.CharField(label='Category')
    search_word = forms.CharField(label='Search Word')
