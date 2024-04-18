from django.urls import path
from .views import CreateProfileView, LoginProfileView, LogoutProfile, ProfileView, ProfileChangeView
from django.contrib.auth import views
from django.urls import reverse_lazy

app_name = 'users'

urlpatterns = [
    # аутентификация и авторизация
    path('register/', CreateProfileView.as_view(), name='register'),
    path('login/', LoginProfileView.as_view(), name='login'),
    path('logout/', LogoutProfile.as_view(), name='logout'),

    path('password-change/',
         views.PasswordChangeView.as_view(template_name='users/registration/password_change_form.html',
                                          success_url=reverse_lazy('users:password_change_done')),
         name='password_change'),
    path('password-change-done/',
         views.PasswordChangeDoneView.as_view(template_name='users/registration/password_change_done.html'),
         name='password_change_done'),

    # профиль
    path('profile/<slug:slug>/', ProfileView.as_view(), name='profile'),
    path('profile/<slug:slug>/update/', ProfileChangeView.as_view(), name='profile_change'),
]
