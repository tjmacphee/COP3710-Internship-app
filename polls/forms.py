from django import forms
from .models import Internship

class InternshipForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        request = kwargs.pop('request', None)
        super(InternshipForm, self).__init__(*args, **kwargs)
        self.fields['user_id'].initial = request.user.id
        
    class Meta:
        model = Internship
        fields = [
            'company',
            'tags',
            'role_description',
            'role',
            'start_dt',
            'end_dt',
            'salary',
        ]
        widgets = {
            'start_dt': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_dt': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
        