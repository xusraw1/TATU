from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from users.models import Profile
from .models import Password, Blog
from .utils import generate_password, get_text, get_parametrs, get_week
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
import requests
from datetime import datetime
from .forms import *


class CreateBlogView(LoginRequiredMixin, View):
    def get(self, request):
        form = CreateBlogForm()
        return render(request, 'services/create_blog.html', {'form': form})

    def post(self, request):
        profile = Profile.objects.get(user=request.user)
        form = CreateBlogForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.profile = profile
            blog.save()
            messages.success(request, 'Пост успешно создан!')
            return redirect('/')
        else:
            messages.error(request, 'Форма заполнена неправильно!')
            return redirect('create_blog')


class Blogs(View):
    def get(self, request):
        blogs = Blog.objects.all().filter(status=True)
        return render(request, 'services/blogs.html', {'blogs': blogs})


class BlogDetailView(View):
    def get(self, request, id):
        form = CreateCommentForm()
        blog = get_object_or_404(Blog, id=id)
        return render(request, 'services/blog.html', {'blog': blog, 'form': form})

    def post(self, request, id):
        form = CreateCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            blog = get_object_or_404(Blog, id=id)
            profile = get_object_or_404(Profile, user=request.user)
            comment.blog = blog
            comment.profile = profile
            comment.save()
            messages.success(request, 'Комментарии успешно создано!')
            return redirect('blog', id)
        messages.error(request, 'Произошла ошибка при заполнении формы комментария!')
        return redirect('blog', id)


class Weather(View):
    def get(self, request):
        key = '0487c90c491a461ab9b93202242804'
        city = request.GET.get('city')
        context = {
            'status': False
        }
        if city:
            url = f'https://api.weatherapi.com/v1/current.json?key={key}&q={city}'
            forecast = f"https://api.weatherapi.com/v1/forecast.json?key={key}&q={city}&days=7"
            new_data = requests.get(forecast)
            if not new_data.status_code == 200:
                messages.info(request, 'Введите существуюший город и попробуйте заново или попозже')
                return redirect('weather')
            data = new_data.json()
            forecast_days = data["forecast"]["forecastday"]
            forecast_info = []

            for day in forecast_days:
                date = day["date"]
                date_obj = datetime.strptime(date, '%Y-%m-%d')
                year = date_obj.year
                month = date_obj.month
                day_number = date_obj.day

                week = get_week(year, month, day_number)

                max_temp_c = day["day"]["maxtemp_c"]
                min_temp_c = day["day"]["mintemp_c"]
                avg_temp_c = day["day"]["avgtemp_c"]
                condition_text = day["day"]["condition"]["text"]
                print(condition_text.rstrip())
                weather_icon = day["day"]["condition"]["icon"]
                max_wind_kph = day["day"]["maxwind_kph"]
                weather_text = get_text(condition_text)
                day_info = {
                    "date": week,
                    "max_temp_c": max_temp_c,
                    "min_temp_c": min_temp_c,
                    "avg_temp_c": avg_temp_c,
                    "condition_text": weather_text,
                    "max_wind_kph": max_wind_kph,
                    "weather_icon": weather_icon,
                    "week": week,
                }
                forecast_info.append(day_info)

            res = requests.get(url)
            if not res.status_code == 200:
                messages.info(request, 'Введите существуюший город и попробуйте заново или попозже')
                return redirect('weather')
            response = res.json()
            context = get_parametrs(response)
            context['data'] = forecast_info
        return render(request, 'services/weather.html', context)


class PasswordViewProfile(LoginRequiredMixin, View):
    def get(self, request, slug):
        profile = get_object_or_404(Profile, slug=slug)
        passwords = Password.objects.filter(profile=profile).order_by('-id')
        context = {
            'profile': profile,
            'passwords': passwords,
        }
        return render(request, 'services/password_list_profile.html', context)

        # нужно добавить к представления генерации паролей несколько фич, оценка пароля и какие символы есть

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


class PasswordView(View):
    def get(self, request):
        top = Password.objects.all().order_by('-id')[:10]
        context = {
            'passwords': top
        }
        return render(request, 'services/password_list.html', context)


def delete_password(request, id):
    slug = None
    password = Password.objects.get(id=id)
    if not request.user == password.profile.user:
        messages.error(request, 'Вы не являетесь создателем этого пароля!')
        return redirect('passwords')
    slug = password.profile.slug
    password.delete()
    messages.error(request, 'Пароль удален.')
    return redirect('password_list', slug)


def services(request):
    return render(request, 'services/services.html')
