from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='doctot_dashboard'),
    path('create_blog/', views.create_blog, name='create_blog'),
    path('<int:blog_id>/edit_blog', views.edit_blog, name='edit_blog'),
    path('<int:blog_id>/delete_blog', views.delete_blog, name='delete_blog'),
    path('available_doctors/', views.available_doctors, name='available_doctors'),
    path('<str:dr_fname>/<str:dr_lname>/book_appointment', views.book_appointment, name='book_appointment'),
    path('<int:apt_id>/appointment_info', views.appointment_info, name='appointment_info'),
    
]

