from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    GENDER = [
        ('man', 'Мужчина'),
        ('woman', 'Женщина')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=150, null=True, blank=True, unique=True)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=5, choices=GENDER, default='Неизвестно', verbose_name='Пол')
    first_name = models.CharField(max_length=50, null=True, blank=True, verbose_name='Имя')
    last_name = models.CharField(max_length=50, null=True, blank=True, verbose_name='Фамилия')

    created = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='Дата создания профиля')
    updated = models.DateTimeField(auto_now_add=True, blank=True, null=True,
                                   verbose_name='Дата последнего обновления профиля')

    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(str(self.username) + str(self.id))
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.username} + {self.email}"

    class Meta:
        ordering = ['-created']
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
        db_table = 'profile'


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.create(
            user=instance,
            username=instance.username,
            email=instance.email
        )