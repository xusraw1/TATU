from django.urls import path
from .views import CreateProfileView, LoginProfileView, LogoutProfile

app_name = 'users'

urlpatterns = [
    path('register/', CreateProfileView.as_view(), name='register'),
    path('login/', LoginProfileView.as_view(), name='login'),
    path('logout/', LogoutProfile.as_view(), name='logout'),
]
