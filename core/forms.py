from django import forms
from .models import Contact, HireRequest

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Name',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Email',
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Subject',
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Your Message',
                'rows': 5,
            }),
        }


class HireRequestForm(forms.ModelForm):
    class Meta:
        model = HireRequest
        fields = ['name', 'email', 'project_type', 'budget', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'project_type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Website, App, Portfolio...'}),
            'budget': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Budget (optional)'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Project Details', 'rows': 5}),
        }