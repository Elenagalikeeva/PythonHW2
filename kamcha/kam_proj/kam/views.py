from django.shortcuts import render, get_object_or_404, redirect
from .models import Kam
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate

def index(request):
    projects = Kam.objects.all()
    return render(request, 'kam/index.html', {'projects': projects})


def blogs(request):
    blogs = Kam.objects.all()
    return render(request, 'kam/blog.html', {'blogs': blogs})


def detail(request, blog_id):
    blog = get_object_or_404(Kam, pk=blog_id)
    return render(request, 'kam/details.html', {'blog': blog})


def kabinet(request):
    return render(request, 'kam/kabinet.html')


def logoutuser(request):
    if request.method == "POST":
        logout(request)
        return redirect('index')



def signupuser(request):
    if request.method == "GET":
        return render(request, 'kam/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1']== request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'],  password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('kab')

            except IntegrityError:
                return render(request, 'kam/signupuser.html', {'form': UserCreationForm(), 'error': \
                    'Такое имя пользователя уже существует. Задайте другое'})

        else:
            return render(request, 'kam/signupuser.html', {'form': UserCreationForm(), 'error':\
                'Пароли не совпадают'})


def loginuser(request):
    if request.method == "GET":
        return render(request, 'kam/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'kam/loginuser.html', {'form':AuthenticationForm(), 'error':\
                    'Неверные данные'})
        else:
            login(request, user)
            return redirect('kab')

