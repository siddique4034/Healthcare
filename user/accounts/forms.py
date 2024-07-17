from django import forms
from .models import Blog
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['user_type', 'title', 'photo', 'content', 'summary']

class UserRegistrationForm(UserCreationForm):
    user_type = models.CharField(max_length=2, choices=Blog.USER_TYPE)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')




Blog.USER_TYPE



