from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import TextInput, PasswordInput
from .models import QRCode, ContactMessage

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username'
    }))
    password = forms.CharField(widget=PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password'
    }))

class QRCodeForm(forms.ModelForm):
    class Meta:
        model = QRCode
        fields = ['data', 'description']
        widgets = {
            'data': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter data for QR code'
            }),
            'description': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter description (optional)'
            }),
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Name', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email', 'class': 'form-control'}),
            'message': forms.Textarea(attrs={'placeholder': 'Your Message', 'class': 'form-control', 'rows': 4}),
        }