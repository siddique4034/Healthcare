from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta

# Create your models here.

class Blog(models.Model):
  CATAEGORY = [
    ('immunization', 'Immunization'),
    ('mental_health', 'Mental health'),
    ('covid_19', 'Covid 19'),
    ('heart_disease', 'Heart disease'),
  ]
  cataegory = models.CharField(max_length=13, choices=CATAEGORY, default='Immunization')
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.CharField(max_length=30)
  photo = models.ImageField(upload_to='photos/', blank=True)
  content = models.TextField(max_length=1000)
  summary = models.TextField(max_length=200)
  is_draft = models.BooleanField(default=False)
  #created_at = models.DateTimeField(auto_now_add=True)
  #updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f'{self.user.username} - {self.title}'
 

class Appointment(models.Model):
  REQUIRED_SPECIALITY = [
    ('immunization', 'Immunization'),
    ('mental_health', 'Mental health'),
    ('covid_19', 'Covid 19'),
    ('heart_disease', 'Heart disease')
  ]
  patient = models.ForeignKey(User, on_delete=models.CASCADE)
  doctor_appointed = models.CharField(max_length=30)
  required_speciacity = models.CharField(max_length=13, choices=REQUIRED_SPECIALITY, default='Immunization')
  appointment_date = models.DateField()
  start_time = models.TimeField()
  end_time = models.TimeField()
  add_event = models.BooleanField()

  def __str__(self):
    return f"{self.required_speciacity}"
  



