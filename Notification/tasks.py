from __future__ import absolute_import, unicode_literals
from django.contrib.auth import get_user_model
from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task(bind=True)
def a_weekly_reminder_to_visit(self):
    #operations
    users = get_user_model().objects.all()
    for user in users:
        mail_subject="Hello from Shop!"
        message="We have new merchandises that may interest you! Visit our website for more information!"
        to_email=user.email
        send_mail(
            subject= mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently=True,
        )
    return 'Done'
