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


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Blog(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    body = RichTextField(verbose_name='Текст')
    image = models.ImageField(upload_to='blog/', default='default.png', verbose_name='Изображение')
    status = models.BooleanField(default=True, verbose_name='Статус')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Созданно')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновленно')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']


class Comment(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    text = models.TextField(max_length=250, verbose_name='Комментарии')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Созданно')

    def __str__(self):
        return f"{self.profile} {self.text[:30]}"

    class Meta:
        ordering = ['-created']