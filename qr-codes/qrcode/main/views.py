from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout
from .forms import RegisterForm  
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def contacts(request):
    return render(request, 'main/contacts.html')

def logout_user(request):
    logout(request)
    return redirect('index')  # Перенаправлення на головну сторінку

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()  # Отримуємо користувача з форми
            login(request, user)  # Передаємо користувача у функцію login
            return redirect('index')  # Перенаправлення на головну сторінку
    else:
        form = AuthenticationForm()
    return render(request, 'main/login.html', {'form': form})

def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = RegisterForm()
    return render(request, 'main/register.html', {'form': form})