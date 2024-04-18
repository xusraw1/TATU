from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) >= 150:
            raise ValidationError("Имя пользователя не должно превышать 150 символов.")
        return username


class LoginForm(forms.Form):
    email = forms.EmailField(label='Эмайл')
    username = forms.CharField(max_length=150, label='Никнейм')
    password = forms.CharField(widget=forms.PasswordInput(), label='Пароль')


class ProfileChangeForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'gender']


class ProfileActivateForm(forms.Form):
    username = forms.CharField(max_length=150, label='Никнейм')
    password = forms.CharField(widget=forms.PasswordInput(), label='Пароль')