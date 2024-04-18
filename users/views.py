from django.shortcuts import render
from django.views.generic.edit import CreateView
from .forms import CreateUserForm, LoginForm
from .models import Profile
from django.urls import reverse_lazy
from django.contrib import messages
from django.views import View


class CreateProfileView(CreateView):
    model = Profile
    template_name = 'users/create_profile.html'
    form_class = CreateUserForm
    success_url = reverse_lazy('register')

    def form_valid(self, form):
        email = form.cleaned_data['email']

        if Profile.objects.filter(email=email).exists():
            messages.error(self.request, 'Пользователь с таким email уже существует.')
            return self.form_invalid(form)

        self.object = form.save()
        messages.success(self.request, 'Профиль успешно создан!')

        return self.form_invalid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Произошла ошибка при создании профиля.')
        return super().form_invalid(form)
