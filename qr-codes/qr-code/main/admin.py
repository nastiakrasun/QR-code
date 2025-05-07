from django.contrib import admin
from .models import QRCode

@admin.register(QRCode)
class QRCodeAdmin(admin.ModelAdmin):
    list_display = ('user', 'data', 'description', 'created_at')  # Поля, які будуть відображатися в списку
    search_fields = ('user__username', 'data')  # Поля для пошуку
    list_filter = ('created_at',)  # Фільтри
