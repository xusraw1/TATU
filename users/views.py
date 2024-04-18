from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .forms import CreateUserForm, LoginForm
from .models import Profile
from django.urls import reverse_lazy
from django.contrib import messages
from django.views import View
from django.contrib.auth import login, authenticate, logout


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
                return redirect('login')
            messages.warning(request, 'Пользователь не найден. Попробуйте войти заново.')
            return redirect('login')
        messages.error(request, 'Форма заполнено неправильно.')
        return redirect('login')


class LogoutProfile(View):
    def get(self, request):
        logout(request)
        messages.success(request, 'Вы вышли из своей учетной записи.')
        return redirect('login')
