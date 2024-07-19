from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
  CATAEGORY = [
    ('Immunization', 'Immunization'),
    ('Mental health', 'mental_health'),
    ('Covid 19', 'covid_19'),
    ('Heart disease', 'heart_disease'),
  ]
  cataegory = models.CharField(max_length=13, choices=CATAEGORY, default='Immunization')
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.CharField(max_length=30)
  photo = models.ImageField(upload_to='photos/', blank=True, null=True)
  content = models.TextField(max_length=1000)
  summary = models.TextField(max_length=200)
  is_draft = models.BooleanField(default=False)
  #created_at = models.DateTimeField(auto_now_add=True)
  #updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f'{self.user.username} - {self.title}'
 