from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout
from .forms import RegisterForm  
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
import qrcode
from django.core.files.base import ContentFile
from io import BytesIO
from .models import QRCode
from .forms import QRCodeForm
import uuid  # Додай імпорт uuid
from django.contrib.auth.decorators import login_required

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

def create_qr_code(request):
    if request.method == 'POST':
        form = QRCodeForm(request.POST)
        if form.is_valid():
            qr_instance = form.save(commit=False)
            qr_instance.user = request.user

            # Генерація QR-коду
            qr = qrcode.make(qr_instance.data)
            buffer = BytesIO()
            qr.save(buffer, format='PNG')

            # Генерація унікальної назви файлу
            unique_filename = f"{uuid.uuid4().hex}.png"
            qr_instance.image.save(unique_filename, ContentFile(buffer.getvalue()), save=False)

            qr_instance.save()
            return redirect('index')  # Перенаправлення після створення
    else:
        form = QRCodeForm()
    return render(request, 'main/create_qr_code.html', {'form': form})

@login_required
def my_qrs(request):
    qrcodes = QRCode.objects.filter(user=request.user)
    return render(request, 'main/my_qrs.html', {'qrcodes': qrcodes})