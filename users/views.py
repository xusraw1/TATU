from django.shortcuts import render
from django.views.generic.edit import CreateView
from .forms import CreateUserForm
from .models import Profile


class CreateProfileView(CreateView):
    model = Profile
    template_name = 'users/create_profile.html'
    form_class = CreateUserForm
