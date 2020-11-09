from django import forms
from django.contrib.auth import login, authenticate

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, request, *args, **kwargs):
        self.request = request
        super(LoginForm, self).__init__(*args, **kwargs)

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