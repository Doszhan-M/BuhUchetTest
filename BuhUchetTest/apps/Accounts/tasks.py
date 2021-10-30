from celery import shared_task
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

from .models import User


@shared_task
def new_password_send_to_email(email, new_password):
    '''Отправка на почту нового пароля.'''
    html_content = render_to_string(
        'new_pass_alert.html', {'new_password': new_password, })
    msg = EmailMultiAlternatives(
        subject=f'Смена пароля',
        from_email=settings.DEFAULT_FROM_EMAIL,
                to=[email, ]
    )
    msg.attach_alternative(html_content, "text/html")
    msg.send()  # отправить
