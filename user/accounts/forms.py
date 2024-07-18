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
    is_doctor = forms.BooleanField(initial=False)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'is_doctor')







