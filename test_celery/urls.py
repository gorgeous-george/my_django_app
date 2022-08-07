from django.urls import path

from test_celery.views import send_email, send_email_failure, send_email_success


urlpatterns = [
    path('', send_email, name="send-email"),
    path('success/', send_email_success, name="send-email-success"),
    path('failure/', send_email_failure, name="send-email-failure"),
]
