from django.shortcuts import render, get_object_or_404
from django.views import View
from users.models import Profile
from .models import Password


class PasswordView(View):
    def get(self, request, slug):
        profile = get_object_or_404(Profile, slug=slug)
        passwords = Password.objects.filter(profile=profile)
        context = {
            'profile': profile,
            'passwords': passwords,
        }
        return render(request, 'services/password_list.html', context)
