from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User

def morning_email_cron_job():
    all_emails = User.objects.values_list('email', flat=True)
    for email in all_emails:
        subject = 'Good Morning Message'
        message = f'Hi, Good Morning'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail( subject, message, email_from, recipient_list)