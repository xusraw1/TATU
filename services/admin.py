from django.contrib import admin
from .models import *


# password
@admin.register(Password)
class PasswordAdmin(admin.ModelAdmin):
    list_display = ['profile', 'created', 'id']

