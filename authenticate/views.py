from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .forms import SignupForm, LoginForm

# Create your views here.


def home(request):
    if 'username' in request.session:
        return redirect('index')
    else:
        return render(request,'home.html')


"""def index(request):
    if 'username' in request.session:
        return redirect('index')
    return render(request, 'index.html')"""


def login(request):
    if 'username' in request.session:
        return redirect('index')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            request.session['username'] = username
            auth.login(request, user)
            return redirect('index')
        else:
            return redirect('login')
    else:
        form = LoginForm()
        dict_forms = {
            'form': form
        }
        return render(request, 'login.html', dict_forms)


def signup(request):
    if 'username' in request.session:
        return redirect('index')
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                print('username taken')
                return redirect('signup')
            elif User.objects.filter(email = email).exists():
                print('email taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(
                    username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                print('user created')
            return redirect('login')
        else:
            print('password not matching')
            return redirect('signup')
    else:
        form = SignupForm()

        dict_forms = {
            'form': form
        }
        return render(request, 'signup.html', dict_forms)


def logout(request):
    if 'username' in request.session:
        request.session.flush()
    auth.logout(request)
    return redirect('/')
