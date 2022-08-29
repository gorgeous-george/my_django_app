from datetime import timedelta

from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone


class SendEmail(forms.Form):
    recipient_email = forms.EmailField(
        label="Recipient's email",
        max_length=100
    )
    subject = forms.CharField(
        label="Email's subject",
        max_length=100
    )
    message_text = forms.CharField(
        widget=forms.Textarea
    )
    email_datetime = forms.DateTimeField()

    # def clean_email_datetime(self):
    #     data = self.cleaned_data['email_datetime']
    #     two_days_limit = timezone.now() + timedelta(hours=48)
    #     current_time = timezone.now()
    #     if not current_time < data < two_days_limit:
    #         raise ValidationError('Please choose another time. Time should be between current and next 48 hours')
    #     return data
