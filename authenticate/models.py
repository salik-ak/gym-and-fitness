from django.db import models

# Create your models here.


class Signup(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    username = models.CharField(max_length=150)
    email = models.EmailField()
    password1 = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)


class Login(models.Model):
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=50)
