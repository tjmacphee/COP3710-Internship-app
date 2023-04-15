from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    company_name = models.CharField(max_length=100)
    contact_email = models.EmailField()
    listings = models.IntegerField()

class Internship(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='internships')
    tags = models.CharField(max_length=200)
    role_description = models.CharField(max_length=200)
    role = models.CharField(max_length=50)
    start_dt = models.DateTimeField()
    end_dt = models.DateTimeField()
    filled = models.IntegerField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)

class User(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    active = models.IntegerField()
    created_dt = models.DateTimeField()
    internship = models.ForeignKey(Internship, on_delete=models.CASCADE, null=True, related_name='user_internship')

class EmailQueue(models.Model):
    subject = models.CharField(max_length=200)
    message = models.CharField(max_length=200)
    processed = models.IntegerField()
    recipient = models.CharField(max_length=100)
