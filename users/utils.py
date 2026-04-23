import random
from django.core.mail import send_mail
from django.conf import settings


def generate_otp(length=4):
   
    return ''.join(str(random.randint(0, 9)) for _ in range(length))


def send_otp_email(email, otp):
    subject = 'Код подтверждения'
    message = f'Ваш одноразовый код: {otp}\nОн действует 5 минут.'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]

    send_mail(
        subject=subject,
        message=message,
        from_email=from_email,
        recipient_list=recipient_list,
        fail_silently=False,
    )