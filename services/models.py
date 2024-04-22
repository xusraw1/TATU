from django.db import models
from users.models import Profile
from django.core.validators import MaxValueValidator, MinValueValidator


class Password(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)
    password = models.CharField(max_length=150, blank=True, null=True, verbose_name='Пароль')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.profile} | {self.rate}"
