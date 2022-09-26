from django.forms import ModelForm
from .models import Post
from django import forms


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'image', 'body')
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title...', 'class': 'form-control'}),
        }
