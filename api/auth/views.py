from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import *
from rest_framework.permissions import IsAuthenticated , AllowAny
from rest_framework.authtoken.models import Token
from rest_framework import status,generics
from users.models import User , PasswordResetOTP
from rest_framework.generics import RetrieveUpdateAPIView, GenericAPIView
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from users.utils import generate_otp, send_otp_email

# @api_view(['POST'])
# def register(request):
#     serializer = RegisterSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     serializer.save()
#     return Response({"message": "Пользователь успешно создан!"})



class RegisterAPIView(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Пользователь успешно создан!"})




@api_view(['POST'])
def login(request):
    serializer = LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    return Response(serializer.validated_data)   # вернёт token, email



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):
    print(request.user)
    Token.objects.filter(user=request.user).delete()
    return Response({"message": "Токен успешно удалён, пользователь разлогинен!"})


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_account(request):
    user = request.user
    Token.objects.filter(user=user).delete()
    user.delete()
    return Response({"message": "Аккаунт успешно удалён!"})


class ProfileAPIView(RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()

    def get_object(self):
        user = self.request.user
        return user
    


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def change_password(request):
    serializer = ChangePasswordSerializer(
        data=request.data, context={'request': request})
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response({"message": "Пароль успешно изменён!"}, 
                    status=status.HTTP_200_OK)
    
    
class RequestOTPview(APIView):
    def post(self, request):
        serializer = RequestOTPSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        user = User.objects.get(email=email)

        PasswordResetOTP.objects.filter(user=user, is_used=False).update(is_used=True)

        otp = generate_otp(4)

        PasswordResetOTP.objects.create(
            user=user,
            otp=otp,
        )

        send_otp_email(email, otp)

        return Response(
            {'message': "OTP отправлен. Действителен 5 минут"},
            status=status.HTTP_200_OK
        )
        
        

class VerifyOTPView(APIView):
    def post(self, request):
        serializer = VerifyOTPSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        otp = serializer.validated_data['otp']

        try:
            user = User.objects.get(email=email)
            otp_obj = PasswordResetOTP.objects.filter(
                user=user,
                otp=otp,
                is_used=False
            ).last()

            if not otp_obj:
                return Response({"error": "Неверный OTP"}, status=400)

            
            return Response({"message": "OTP подтвержден"}, status=200)

        except User.DoesNotExist:
            return Response({"error": "Пользователь не найден"}, status=404)
        

class ResetPasswordView(APIView):
    def post(self, request):
        serializer = ResetPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        otp = serializer.validated_data['otp']
        new_password = serializer.validated_data['new_password']

        try:
            user = User.objects.get(email=email)
            otp_obj = PasswordResetOTP.objects.filter(
                user=user,
                otp=otp,
                is_used=False
            ).last()

            if not otp_obj:
                return Response({"error": "Неверный OTP"}, status=400)

            
            user.set_password(new_password)
            user.save()

            
            otp_obj
            otp_obj.is_used = True
            otp_obj.save()

            return Response({"message": "Пароль успешно обновлен"}, status=200)

        except User.DoesNotExist:
            return Response({"error": "Пользователь не найден"}, status=404)