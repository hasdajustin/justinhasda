from django.shortcuts import render, redirect
from .models import Project, HireRequest
from .forms import ContactForm, HireRequestForm
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'layouts/index.html')

def projects(request):
    projects = Project.objects.order_by('-created_at')
    return render(request, 'layouts/projects.html', {'projects': projects})

def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect('contact')
    return render(request, 'layouts/contact.html', {'form': form})

def hire_me(request):
    form = HireRequestForm()
    if request.method == 'POST':
        form = HireRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you! I'll get back to you soon.")
            return redirect('hire_me')
    return render(request, 'layouts/hire_me.html', {'form': form})