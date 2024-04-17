from django.urls import path
from .views import CreateProfileView

urlpatterns = [
    path('register/', CreateProfileView.as_view(), name='register'),
]
