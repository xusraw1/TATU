from django.urls import path
from .views import CreateProfileView, LoginProfileView, LogoutProfile, ProfileView

app_name = 'users'

urlpatterns = [
    # аутентификация и авторизация
    path('register/', CreateProfileView.as_view(), name='register'),
    path('login/', LoginProfileView.as_view(), name='login'),
    path('logout/', LogoutProfile.as_view(), name='logout'),

    # профиль
    path('profile/<slug:slug>/', ProfileView.as_view(), name='profile'),
]
