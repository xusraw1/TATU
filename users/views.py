from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .forms import CreateUserForm, LoginForm, ProfileChangeForm
from .models import Profile
from django.urls import reverse_lazy
from django.contrib import messages
from django.views import View
from django.contrib.auth import login, authenticate, logout


class ProfileView(View):
    def get(self, request, slug):
        try:
            profile = Profile.objects.get(slug=slug)
        except Profile.DoesNotExist as e:
            messages.error(request, 'Профиль не найден!')
            return redirect('main:index')
        return render(request, 'users/profile.html', {'profile': profile})


class ProfileChangeView(View):
    def get(self, request, slug):
        try:
            profile = Profile.objects.get(slug=slug)
        except Profile.DoesNotExist as e:
            messages.error(request, 'Профиль не найден!')
            return redirect('main:index')
        form = ProfileChangeForm(instance=profile)
        return render(request, 'users/change_profile.html', {'form': form, 'profile': profile})

    def post(self, request, slug):
        profile = Profile.objects.get(slug=slug)
        form = ProfileChangeForm(request.POST, instance=profile)
        if form.is_valid():
            form.save(commit=False)
            form.instance.user = profile.user  # Устанавливаем user для instance формы
            form.save()
            messages.success(request, 'Профиль успешно изменен.')
            return redirect('users:profile', profile.slug)
        messages.error(request, 'Не удалось обновить профиль. Попробуйте ввести корректные данные!')
        return render(request, 'users/change_profile.html', {'form': form, 'profile': profile})


class CreateProfileView(CreateView):
    model = Profile
    template_name = 'users/create_profile.html'
    form_class = CreateUserForm
    success_url = reverse_lazy('main:index')

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


class LoginProfileView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'users/login_profile.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Вы успешно вошли в свою учетную запись.')
                return redirect('main:index')
            messages.warning(request, 'Пользователь не найден. Попробуйте войти заново.')
            return redirect('users:login')
        messages.error(request, 'Форма заполнено неправильно.')
        return redirect('users:login')


class LogoutProfile(View):
    def get(self, request):
        logout(request)
        messages.info(request, 'Вы вышли из своей учетной записи.')
        return redirect('users:login')
