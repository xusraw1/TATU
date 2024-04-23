from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from users.models import Profile
from .models import Password
from .utils import generate_password
from django.http import HttpResponse
from django.contrib import messages


class PasswordView(View):
    def get(self, request, slug):
        profile = get_object_or_404(Profile, slug=slug)
        passwords = Password.objects.filter(profile=profile).order_by('-id')
        context = {
            'profile': profile,
            'passwords': passwords,
        }
        return render(request, 'services/password_list.html', context)

    def post(self, request, slug):
        range = request.POST.get('range')
        chars_upper = request.POST.get('chars_upper')
        chars_lower = request.POST.get('chars_lower')
        nums = request.POST.get('nums')
        characters = request.POST.get('characters')

        password = generate_password([range, chars_lower, chars_upper, nums, characters])

        profile = get_object_or_404(Profile, slug=slug)
        create_password = Password.objects.create(profile=profile, password=password)

        messages.success(request, 'Пароль сгенерирован успешно.')

        return redirect('password_list', slug)


def delete_password(request, id):
    slug = None
    password = Password.objects.get(id=id)
    slug = password.profile.slug
    password.delete()
    messages.error(request, 'Пароль удален.')
    return redirect('password_list', slug)
