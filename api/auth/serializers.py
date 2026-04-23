from rest_framework import serializers
from django.contrib.auth.password_validation import *
from rest_framework.authtoken.models import Token
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate
from users.models import User

class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email','first_name','last_name','password','password2')

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username занят")
        return value


    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email уже используется")
        return value

    
    def validate(self, attrs):
        if attrs.get('password') != attrs.get('password2'):
            raise serializers.ValidationError("Пароли не совпадают")
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        return User.objects.create_user(**validated_data)
    
    def validate_password(self, value):
     if len(value) < 8:
        raise serializers.ValidationError("Минимум 8 символов")

     has_digit = False
     has_upper = False
     has_lower = False
     has_special = False

     for char in value:
        if char.isdigit():
            has_digit = True
        elif char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif not char.isalnum():
            has_special = True

     if not has_digit:
        raise serializers.ValidationError("Добавь хотя бы одну цифру")
     if not has_upper:
        raise serializers.ValidationError("Добавь заглавную букву")
     if not has_lower:
        raise serializers.ValidationError("Добавь строчную букву")
     if not has_special:
        raise serializers.ValidationError("Добавь специальный символ")

     return value
 
 
 
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        user = authenticate(
            username=attrs['email'],
            password=attrs['password']
        )

        if not user:
            raise serializers.ValidationError("Неверный email или пароль")

        token, _ = Token.objects.get_or_create(user=user)

        return {
            "token": token.key,
            "email": user.email
        }
        
        
        
        
        
    
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'phone_number', "bio",
                   "avatar",)
        read_only_fields = ('email',) 


# Change Password
class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(
        write_only=True, 
        validators=[validate_password]
    )

    def validate(self, attrs):
        user = self.context['request'].user
        if not user.check_password(attrs['old_password']):
            raise serializers.ValidationError(
                "Старый пароль неверный")
        return attrs

    def save(self, **kwargs):
        user = self.context['request'].user
        user.set_password(
            self.validated_data['new_password'])
        user.save()
        return user
    
    
    
class RequestOTPSerializer(serializers.Serializer):
    email = serializers.EmailField()
    
    def validate_email(self,value):
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                "Пользователь с этим электронной почтой не найден"
            )
        return value
    

class VerifyOTPSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=6)
    
    
class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=6)
    new_password = serializers.CharField(min_length=8)