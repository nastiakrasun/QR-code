from django.contrib import admin
from .models import QRCode, ContactMessage

@admin.register(QRCode)
class QRCodeAdmin(admin.ModelAdmin):
    list_display = ('user', 'data', 'description', 'created_at')  # Поля, які будуть відображатися в списку
    search_fields = ('user__username', 'data')  # Поля для пошуку
    list_filter = ('created_at',)  # Фільтри

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'created_at')
    search_fields = ('name', 'email', 'message')
    list_filter = ('created_at',)
