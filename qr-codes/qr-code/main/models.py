from django.db import models
from django.contrib.auth.models import User

class QRCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='qrcodes')  # Зв'язок із користувачем
    data = models.TextField()  # Дані, які будуть закодовані в QR-код
    description = models.CharField(max_length=1000, blank=True)  # Опис QR-коду
    image = models.ImageField(upload_to='qr-images/')  # Збереження зображення QR-коду
    created_at = models.DateTimeField(auto_now_add=True)  # Дата створення

    def __str__(self):
        return f"QR Code for {self.user.username} - {self.created_at}"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.email})"
