from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

from polls.models import Internship

from .forms import InternshipForm

# Create your views here.


# Define the dashboard handler
def dashboard(request):
    if request.method == 'POST': # If the form has been submitted...
        form = InternshipForm(request.POST)
        if form.is_valid(): # All validation rules pass
            form.save() # Save the form data to the database
            return redirect('dashboard') # Redirect after POST
    else:
        form = InternshipForm() # Create an empty form
    
    internships = Internship.objects.all() # Get all the internships
    context = {'form': form, 'internships': internships} # Create a context dictionary
    return render(request, "dashboard.html", context) # Render the template


# Define the login action
def login(request):
    return redirect('dashboard')



# Define the add_internship view
def add_internship(request):
    form = InternshipForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {'form': form}
    return render(request, 'add_internship.html', context)