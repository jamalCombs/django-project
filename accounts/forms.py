from django import forms
from django.forms import widgets
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .models import User


class LoginForm(forms.Form):
    username = forms.CharField(label='')
    password = forms.CharField(label='')

    def __init__(self, request, *args, **kwargs):
        self.request = request
        super(LoginForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget = widgets.TextInput(
            attrs = {
                'class': 'form-group',
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Username',
                'id': 'inputUsername',
                })

        self.fields['password'].widget = widgets.PasswordInput(
            attrs = {
                'class': 'form-group',
                'class': 'form-control',
                'type': 'password',
                'placeholder': 'Password',
                'id': 'inputPassword',
                })

    def clean(self):
        request = self.request
        data = self.cleaned_data
        username = data.get('username')
        password = data.get('password')

        user = authenticate(request, username=username, password=password)

        if user is None:
            raise forms.ValidationError('Invalid credentials')

        login(request, user)
        self.user = user
        
        return data


class RegisterForm(forms.ModelForm):
    username = forms.CharField(label='')
    email = forms.EmailField(label='')
    password = forms.CharField(label='', widget=forms.PasswordInput)
    confirmed_password = forms.CharField(label='', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'full_name',
            'email'
        ]
        labels = {
            'full_name': '',
            'email': ''
        }
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-group',
                'type': 'text',
                'class': 'form-scontrol',
                'placeholder': 'Full Name',
                'id': 'inputName'
                }),
            'email': forms.EmailInput(attrs={
                'class': 'form-group',
                'type': 'email',
                'class': 'form-control',
                'placeholder': 'Email Address',
                'id': 'inputEmail'
                }),
            'username': forms.TextInput(attrs={
                'class': 'form-group',
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Username',
                'id': 'inputUsername'
                }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-group',
                'class': 'form-control',
                'type': 'password',
                'placeholder': 'Password',
                'id': 'inputPassword'
                }),
            'confirmed_password': forms.PasswordInput(attrs={
                'class': 'form-group',
                'class': 'form-control',
                'type': 'password',
                'placeholder': 'Confirmed Password',
                'id': 'inputPassword'
                })

        }

    def clean(self):
        data = self.cleaned_data
        username = data.get('username')
        password = data.get('password')
        confirmed_password = data.get('confirmed_password')

        if confirmed_password != password:
            raise forms.ValidationError('Passwords must match')
        
        return data
