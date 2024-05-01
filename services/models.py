from django.db import models
from users.models import Profile
from django.core.validators import MaxValueValidator, MinValueValidator
from ckeditor.fields import RichTextField

()


class Password(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)
    password = models.CharField(max_length=150, blank=True, null=True, verbose_name='Пароль')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.profile}"


class Blog(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = RichTextField()
    image = models.ImageField(upload_to='blog/', default='default.png')
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']
