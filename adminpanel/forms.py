from authenticate.models import Signup
from django import forms
from .models import AdminLogin


class AdminLoginForm(forms.ModelForm):

    class Meta:
        model = AdminLogin
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput(attrs={'placeholder': 'Enter your password'}),
            'username': forms.TextInput(attrs={'placeholder': 'Enter your username'})

        }

        labels = {
            'username': 'username',
            'password': 'password',
        }


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Signup
        fields = ['first_name', 'last_name', 'username', 'email']
        labels = {
            'first_tname': 'first name',
            'last_name': 'last name',
            'username': 'username',
            'email': 'email',
        }
