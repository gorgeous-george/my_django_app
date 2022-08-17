from django.views.decorators.cache import cache_page
from django.urls import path

from test_celery.views import QuoteView, send_email, send_email_failure, send_email_success

urlpatterns = [
    path('', send_email, name="send-email"),
    path('success/', send_email_success, name="send-email-success"),
    path('failure/', send_email_failure, name="send-email-failure"),
    path('cached_quotes/', cache_page(10)(QuoteView.as_view()), name="cached-quotes"),
]
