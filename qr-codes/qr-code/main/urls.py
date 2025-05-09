from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about),
    path('contacts', views.contacts),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('register', views.register_user, name='register'),
    path('create_qr', views.create_qr_code, name='create_qr'),
    path('delete_qr/<int:qr_id>/', views.delete_qr_code, name='delete_qr'),
    path('my_qrs', views.my_qrs, name='my_qrs'),
]