from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True, label="Username", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter your Username'}))
    first_name = forms.CharField(max_length=30, required=False, label="First Name",
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your first name'}))
    last_name = forms.CharField(max_length=30, required=False, label="Last Name",
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your last name'}))
    email = forms.EmailField(required=False, label="Email",
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}))
    password1 = forms.CharField(label="Password", widget=(forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter your password'})))
    password2 = forms.CharField(
        label="Confirm Password", widget=(forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm your password'})))

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name",
                  'email', 'password1', 'password2']
