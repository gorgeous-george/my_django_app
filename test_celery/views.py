from datetime import timedelta

from django.contrib import messages
from django.shortcuts import redirect, render
from django.utils import timezone
from django.views.generic import ListView

from test_celery.forms import SendEmail
from test_celery.models import Quote
from test_celery.tasks import send_email_task


def send_email(request):
    data = dict()
    if request.method == 'POST':
        form = SendEmail(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message_text = form.cleaned_data['message_text']
            recipient_email = form.cleaned_data['recipient_email']
            # email_datetime = form.cleaned_data['email_datetime'] + timedelta(hours=3)  # todo: FIND WAY TO AVOID TIMEZONE BUG
            # send_email_task.apply_async((subject, message_text, recipient_email), eta=email_datetime)
            send_email_task.delay(subject, message_text, recipient_email)
            messages.add_message(request, messages.SUCCESS, 'Message sent')
            # return redirect('/send_email/success/')
            return redirect('/send_email/')
    else:
        form = SendEmail(initial={"email_datetime": timezone.now()})
    return render(
        request,
        "test_celery/index.html",
        {
            "form": form,
        }
    )


def send_email_success(request):
    return render(request, "test_celery/index.html")


def send_email_failure(request):
    return render(request, "test_celery/failure.html")


class QuoteView(ListView):
    model = Quote
    queryset = Quote.objects.select_related("authors")
    paginate_by = 1000
