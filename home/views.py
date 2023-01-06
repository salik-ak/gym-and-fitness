from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AdmissionForm
from .models import Course, Trainers
from django.contrib.auth.models import auth
from .models import Course, Trainers

# Create your views here.


def index(request):
    if 'username' in request.session:
        return render(request, 'index.html')
    else:
        return redirect('home')


def about(request):
    if 'username' in request.session:
        return render(request, "about.html")
    else:
        return redirect('home')


def admission(request):
    if 'username' in request.session:
        if request.method == "POST":
            form = AdmissionForm(request.POST)
            if form.is_valid():
                form.save()
                return render(request, 'confirmation.html')
        form = AdmissionForm()
        dict_form = {
            'form': form
        }
        return render(request, "admission.html", dict_form)
    else:
        return redirect('home')


def trainers(request):
    if 'username' in request.session:

        dict_tainers = {
            'trainers': Trainers.objects.all()
        }
        return render(request, "trainers.html", dict_tainers)
    else:
        return redirect('home')


def course(request):
    if 'username' in request.session:

        dict_course = {
            'cours': Course.objects.all()
        }
        return render(request, "course.html", dict_course)
    else:
        return redirect('home')


def logout(request):
    if 'username' in request.session:
        request.session.flush()
    auth.logout(request)
    return redirect('/')
