from django.urls import path
from .views import *

urlpatterns = [
    path('password/list/<slug:slug>/', PasswordView.as_view(), name='password_list'),
    path('password/delete/<int:id>/', delete_password, name='password_delete'),
]
