from .models import Profile
from django import forms
from django.forms import TextInput, ClearableFileInput


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['nickname', 'my_image', 'address']
        labels = {
            'nickname': '닉네임',
            'my_image': '이미지',
            'address': '주소',
        }
        widgets ={
            'nickname': TextInput(attrs={
                'style':'margin-top:10%;',
                'style': 'margin-bottom:10%;'
            }),
            'my_image': ClearableFileInput(attrs={
                'style':'margin-top:5%;'
            }),
            'address': TextInput(attrs={
                'style': 'margin-top:10%;'
            })
        }
