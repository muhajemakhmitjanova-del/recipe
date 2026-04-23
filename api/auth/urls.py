from django.urls import path

from .views import *

urlpatterns = [
    path("register/", RegisterAPIView.as_view()),
    path("login/", login),
    path("logout/", logout),
    path('delete-account/', delete_account),
    path("profile/", ProfileAPIView.as_view()),
    path("change-password/", change_password),
    path('password/',RequestOTPview.as_view()),
    path('verify_otp/', VerifyOTPView.as_view()),
    path('reset_password/', ResetPasswordView.as_view()),
]