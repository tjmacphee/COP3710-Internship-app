from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

# Define the URL patterns for the polls app
urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path('add_internship/', views.add_internship, name='add_internship'),
    path('login/', views.login, name='login'),
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='loginview'),
]