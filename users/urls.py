from django.urls import path
from .views import CreateProfileView, LoginProfileView

urlpatterns = [
    path('register/', CreateProfileView.as_view(), name='register'),
    path('login/', LoginProfileView.as_view(), name='login'),
]
