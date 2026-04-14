from django.db import models
from django.contrib.auth.models import AbstractUser

from django_resized import ResizedImageField
from phonenumber_field.modelfields import PhoneNumberField

from .managers import UserManager


class User(AbstractUser):
    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        ordering = ('-date_joined',)

    username = None

    email = models.EmailField(unique=True)
    
    avatar = ResizedImageField(
        upload_to='users/avatars/',
        crop=['middle', 'center'],
        size=[300, 300],
        quality=90,
        null=True,
        blank=True
    )

    phone_number = PhoneNumberField(unique=True, blank=True)

    bio = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email or str(self.id)