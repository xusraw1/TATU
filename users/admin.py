from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        'username',
        'email',
        'slug',
        'gender',
        'created',
    ]
    list_filter = [
        'gender',
        'created',
    ]
    list_editable = ['gender']
