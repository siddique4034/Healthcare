from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='doctot_dashboard'),
    path('create_blog/', views.create_blog, name='create_blog')

    
]

