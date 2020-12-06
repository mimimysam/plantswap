from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Account

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=100, help_text='Email is required.')
    first_name = forms.CharField(max_length=100, help_text='First name is required.')
    last_name = forms.CharField(max_length=100, help_text='Last name is required.')
    address = forms.CharField(max_length=100, help_text='Address is required.')
    city = forms.CharField(max_length=100, help_text='City is required.')
    state = forms.CharField(max_length=50, help_text='State is required.')
    zip_code = forms.CharField(max_length=20, help_text='Zip code is required.')
    birthday = forms.CharField(max_length=100, help_text='Birthday is required.')

    class Meta:
        model = Account
        fields = ('email', 'first_name', 'last_name', 'address', 'city', 'state', 'zip_code', 'birthday', 'password1', 'password2')
        