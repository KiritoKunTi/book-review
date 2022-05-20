from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import *
from django.forms.models import ModelForm

class CustomRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=254, widget=forms.TextInput({'placeholder': 'Username'}))
    password1 = forms.CharField(widget=forms.PasswordInput({'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput({'placeholder': 'Confirm Password'}))
    email = forms.EmailField(widget=forms.EmailInput({'placeholder': 'Email'}))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']

class ProfileForm(ModelForm):       
    class Meta:
        model = Profile
        # fields = '__all__'
        exclude = ('user',)
        