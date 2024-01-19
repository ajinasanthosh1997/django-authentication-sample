# auth_app/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import *

class SignUpForm(UserCreationForm):
    # Add any additional fields if needed
    class Meta:
        model = CustomUser
        fields = ('username','email', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    # You can customize this form if needed
    pass
