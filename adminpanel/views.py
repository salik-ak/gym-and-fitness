

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .forms import AdminLoginForm, UpdateForm
from home.models import Admissions, Trainers


# Create your views here.
def adminlogin(request):
    if 'username' in request.session:
        return redirect('adminhome')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            request.session['username'] = username
            if user.is_superuser:

                auth.login(request, user)

                return redirect('adminhome')
            else:
                return redirect('adminlogin')
        else:
            return redirect('adminlogin')
    else:
        form = AdminLoginForm()
        dict_forms = {
            'form':form
        }

        return render(request,'adminlogin.html',dict_forms)

def adminhome(request):
    if 'username' in request.session:
        seb = User.objects.all()
        admission = Admissions.objects.all()
        trainers = Trainers.objects.all()