from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.


# Define the dashboard view
def dashboard(request):
    return render(request, "dashboard.html")


# Define the login action
def login(request):
    return redirect('dashboard')
