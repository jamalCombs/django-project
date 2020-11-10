from django import forms
from django.forms import widgets
from django.contrib.auth import login, authenticate

class LoginForm(forms.Form):
    email = forms.EmailField(label='', max_length=75)
    password = forms.CharField(label='')

    def __init__(self, request, *args, **kwargs):
        self.request = request
        super(LoginForm, self).__init__(*args, **kwargs)

        self.fields['email'].widget = widgets.EmailInput(
            attrs = {
                'class': 'form-group',
                'type': 'email',
                'class': 'form-control',
                'placeholder': 'Email',
                'id': 'inputEmail',
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
        email = data.get('email')
        password = data.get('password')

        user = authenticate(request, username=email, password=password)

        if user is None:
            raise forms.ValidationError('Invalid credentials')

        login(request, user)
        self.user = user
        
        return data