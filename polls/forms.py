from django import forms
from .models import Internship

class InternshipForm(forms.ModelForm):
    class Meta:
        model = Internship
        fields = [
            'company',
            'user',
            'tags',
            'role_description',
            'role',
            'start_dt',
            'end_dt',
            'filled',
            'salary',
        ]