from django.urls import path
from .views import *

urlpatterns = [
    path('passwords/', PasswordView.as_view(), name='passwords'),

    path('password/list/<slug:slug>/', PasswordViewProfile.as_view(), name='password_list'),
    path('password/delete/<int:id>/', delete_password, name='password_delete'),

    path('', services, name='services'),
]
