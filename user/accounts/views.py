from django.shortcuts import render
from .forms import BlogForm, UserRegistrationForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Blog

# Create your views here.
def home_page(request):
        return render(request, 'accounts/home_page.html')

def register(request):
        if request.method == 'POST':
                form = UserRegistrationForm(request.POST, request.FILES)
                if form.is_valid():
                        user = form.save(commit=False)
                        user.save(request, user)
                        login(request, user)
                        return redirect('home_page')
        else:
                form = UserRegistrationForm()
        return render(request, 'registration/register.html', {'form': form}) 

 