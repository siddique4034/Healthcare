from django.shortcuts import render
from django.http import HttpResponse
from .forms import BlogForm, UserRegistrationForm, AppointmentForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import Blog, User, Appointment
from datetime import datetime, timedelta
from event_creator import create_event


# Create your views here.
@login_required
def home_page(request):
         if (request.user.is_staff == True):
                dr_apt = Appointment.objects.filter(doctor_appointed=f"{request.user.first_name} {request.user.last_name}")
                return render(request, 'accounts/home_page.html', {'apts': dr_apt})
         elif (request.user.is_staff == False):
                pt_apt = Appointment.objects.filter(patient=request.user)
                return render(request, 'accounts/home_page.html', {'apts': pt_apt})


def register(request):
        if request.method == 'POST':
                form = UserRegistrationForm(request.POST, request.FILES)
                if form.is_valid():
                        user = form.save(commit=False)
                        user.save()
                        login(request, user)
                        return redirect('home_page')
        else:
                form = UserRegistrationForm()
        return render(request, 'registration/register.html', {'form': form}) 


@login_required
def dashboard(request):
        blog = Blog.objects.filter(is_draft=False)
        if (request.user.is_staff == True):
                return render(request, 'accounts/doctor_dashboard.html', {'blogs': blog})
        else:
                return render(request, 'accounts/patient_dashboard.html', {'blogs': blog})


@login_required
def create_blog(request):
        if (request.user.is_staff == True):
                if request.method == 'POST':
                        form = BlogForm(request.POST, request.FILES)
                        if form.is_valid():
                                blog = form.save(commit=False)
                                blog.user = request.user
                                blog.save()
                                return redirect('../dashboard/')               
                else:
                        form = BlogForm()
                        return render(request, 'accounts/create_blog.html', {'form': form})
        else:
                return HttpResponse("Login as Doctor to create post !!!")


@login_required
def edit_blog(request, blog_id):
        if (request.user.is_staff == True):
                blog_post = get_object_or_404(Blog, pk=blog_id, user=request.user)
                if request.method == 'POST':
                        form = BlogForm(request.POST, request.FILES, instance=blog_post)
                        if form.is_valid():
                                blog = form.save(commit=False)
                                blog.user = request.user
                                blog.save()
                                return redirect('../../dashboard')
                else:
                        form = BlogForm(instance=blog_post)
                return render(request, 'accounts/edit_blog.html', {'form': form})


@login_required
def delete_blog(request, blog_id):
        blog = get_object_or_404(Blog, pk=blog_id, user=request.user)
        if request.method == 'POST':
                blog.delete()
                return redirect('../../dashboard')
        return render(request, 'accounts/delete_confirmation_page.html', {'blog': blog})


@login_required
def available_doctors(request):      
        if (request.user.is_staff == False):
                doctors_list = User.objects.filter(is_staff=True)
                return render(request, 'accounts/available_doctors.html', {'doctors': doctors_list})
        else:
                return HttpResponse("Login as Patient to see available doctors !!!!")


@login_required
def book_appointment(request, dr_fname, dr_lname):
        if (request.user.is_staff == False):
                apt_form = AppointmentForm(request.POST)
                if (request.method == 'POST'):
                        doctor = f"{dr_fname} {dr_lname}"
                        apt = apt_form.save(commit=False)
                        apt.patient = request.user
                        apt.doctor_appointed = doctor
                        
                        start_time = datetime.strptime(f"{apt.start_time}", "%H:%M:%S")
                        end_time = start_time + timedelta(minutes=45)
                        apt.end_time = end_time
                        apt.save()
                        pt_email = User.objects.filter(username=request.user)[0].email
                        dr_email = User.objects.filter(first_name=dr_fname)[0].email
                        create_event(apt=apt, pt_email=pt_email, dr_email=dr_email)
                        return redirect(f'../../{apt.id}/appointment_info')
                else:
                        apt_form = AppointmentForm()
                        return render(request, 'accounts/appointment_form.html', {'form': apt_form})


@login_required
def appointment_info(request, apt_id):
        if (request.user.is_staff == False):
                apt_info = Appointment.objects.filter(pk=apt_id)
                return render(request, 'accounts/appointment_info.html', {'info': apt_info})


