from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
  USER_TYPE = [
    ('Dr', 'Doctor'),
    ('Pt', 'Patient'),
  ]
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.CharField(max_length=30)
  photo = models.ImageField(upload_to='photos/', blank=True, null=True)
  content = models.TextField(max_length=500)
  summary = models.TextField(max_length=100)
  user_type = models.CharField(max_length=2, choices=USER_TYPE, default='Dr')
  #created_at = models.DateTimeField(auto_now_add=True)
  #updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f'{self.user.username} - {self.title}'
 