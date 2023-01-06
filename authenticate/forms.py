from django import forms
from .models import Signup, Login


class SignupForm(forms.ModelForm):

    class Meta:
        model = Signup
        fields = '__all__'
        widgets = {
            'password1': forms.PasswordInput(attrs={'placeholder': 'Enter your password'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Confirm your password'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter your firstname'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter your lastname'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your Email'}),
            'username': forms.TextInput(attrs={'placeholder': 'Enter your username'})
        }

        labels = {
            'firs_tname': 'first name',
            'last_name': 'last name',
            'username': 'username',
            'email': 'email',
            'password1': 'password',
            'password2': 'password',

        }


class LoginForm(forms.ModelForm):

    class Meta:
        model = Login
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput(attrs={'placeholder': 'Enter your password'}),
            'username': forms.TextInput(attrs={'placeholder': 'Enter your username'}),

        }

        labels = {
            'username': 'username',
            'password': 'password',
        }
