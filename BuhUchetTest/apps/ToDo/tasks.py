from celery import shared_task
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

from apps.Accounts.models import User


@shared_task
def execution_change_alert(headline, execute):
    '''Уведомление на почту о смене статуса выполнения задачи.'''

    if execute:
        status = 'Выполнен'
    else:
        status = 'Не выполнен'
    html_content = render_to_string('execution_alert.html', {
                                    'headline': headline, 'status': status})

    emails = [user.email for user in User.objects.all()]
    msg = EmailMultiAlternatives(
        subject=f'Выполнение задачи',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=emails
    )
    msg.attach_alternative(html_content, "text/html")
    msg.send()  # отправить
