from django.shortcuts import render
from django.http import HttpResponse
from .forms import BlogForm, UserRegistrationForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import Blog

# Create your views here.
@login_required
def home_page(request):
        return render(request, 'accounts/home_page.html')

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
        if (request.user.username== "Nafis") or (request.user.username=="Siddique"):
                return render(request, 'accounts/doctor_dashboard.html', {'blogs': blog})
        else:
                return render(request, 'accounts/patient_dashboard.html', {'blogs': blog})

@login_required
def create_blog(request):
        if (request.user.username== "Nafis") or (request.user.username=="Siddique"):
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
                return HttpResponse ("Login as Doctor to create post !!!")

@login_required
def edit_blog(request, blog_id):
        if (request.user.username== "Nafis") or (request.user.username=="Siddique"):
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





