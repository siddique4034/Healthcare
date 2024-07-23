from django import forms
from .models import Blog, Appointment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['cataegory', 'title', 'photo', 'content', 'summary', 'is_draft']


class UserRegistrationForm(UserCreationForm):
    is_doctor = forms.BooleanField(initial=False)
    #photos = forms.ImageField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'date_joined', 'is_doctor')


class AppointmentForm(forms.ModelForm):
    add_event = forms.BooleanField(initial=False, required=False)
    class Meta:
        model = Appointment
        fields = ['required_speciacity', 'appointment_date', 'start_time', 'add_event']




