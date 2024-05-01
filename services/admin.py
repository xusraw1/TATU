from django.contrib import admin
from .models import *


# password
@admin.register(Password)
class PasswordAdmin(admin.ModelAdmin):
    list_display = ['profile', 'created', 'id']


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['profile', 'created', 'status']
    search_filters = ['title', 'body']
