from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

from polls.models import Internship
from polls.models import Company

from .forms import InternshipForm

from django.contrib.auth.hashers import make_password

from django.contrib.auth.decorators import login_required
from django.db.models import F, Value
from django.db.models.functions import Coalesce

# Create your views here.


# Define the dashboard handler
def dashboard(request):
    form = InternshipForm() # Create a form instance
    # get internships and inner join with companies
    internships = Internship.objects.select_related('company').annotate(
    company_name=F('company__company_name')
)

    companies = Company.objects.all()
    context = {'form': form, 'internships': internships, 'companies': companies} # Create a context dictionary
    return render(request, "dashboard.html", context) # Render the template


# Define the login action
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            context = {'error_message': 'Invalid credentials'}
            return render(request, 'login.html', context)
    else:
        return render(request, 'login.html')



# Define the add_internship controller
def add_internship(request):
    form = InternshipForm(request.POST, request=request)
    if form.is_valid(): # All validation rules pass
        print("Form is valid")
        print(make_password('password'))
        internship = form.save(commit=False)
        internship.user_id = 1  # Set the user_id to the current user's ID
        internship.filled = 0
        internship.save()
        return redirect('dashboard')
    else:
        # If form is not valid, show error message in the context of the dashboard view
        print("Form is not valid")
        print(form.errors)
        internships = Internship.objects.all() # Get all the internships
        companies = Company.objects.all() # Get all the companies
        context = {'form': form, 'internships': internships, 'companies': companies} # Create a context dictionary
        return render(request, "dashboard.html", context) # Render the template``