from django.db import models
from django.contrib.auth.models import AbstractUser,PermissionManager

from .managers import UserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from datetime import timedelta


class User(AbstractUser):
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        ordering = ['-date_joined']
    
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True, verbose_name='Электронная почта', blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, verbose_name='Аватар')
    phone_number = PhoneNumberField(blank=True, null=True, verbose_name='Номер телефона')
    bio = models.TextField(verbose_name = 'о себе',null = True,blank = True)
    
    
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email or self.first_name}'
    
    
    
    
class PasswordResetOTP(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    otp = models.CharField(max_length= 4)
    is_used = models.BooleanField(default=False)
    is_verified = models.BooleanField(default = False)
    created_at = models.DateField(auto_now_add=True)
    expires_at = models.DateTimeField()
    
    class Meta:
        verbose_name = 'Password Reset OTP'
        ordering = ['-created_at']
        
    def save(self,*args,**kwargs):
        if not self.expires_at:
            self.expires_at = timezone.now()+timedelta(minutes=5)
        super().save(*args,**kwargs)
        
        
    def is_exspired(self):
        return timezone.now()>self.expires_at
    
    def __str__(self):
        return f'{self.user.email} - {self.otp}'