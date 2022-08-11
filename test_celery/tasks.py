import requests

from bs4 import BeautifulSoup

from celery import shared_task

from django.core.mail import send_mail

from test_celery.models import Author, Quote


@shared_task
def send_email_task(subject, message_text, recipient_email):
    send_mail(
        subject,
        message_text,
        'test@abc.com',
        [recipient_email],
        fail_silently=False,
    )


@shared_task
def parse_5_quotes():
    base_url = 'https://quotes.toscrape.com/'
    r = requests.get(base_url)
    soup = BeautifulSoup(r.content, 'html.parser')
    next_button_url = soup.find('li', {'class': 'next'}).a.get('href')
    # loop for pagination
    while True:
        # counter to stop the loop after 5 quotes saved
        counter = 0
        while counter != 5:
            # take all quotes on the page
            parsed_quotes = soup.find_all('div', {'class': 'quote'})
            # iteration through each quote on the page
            for quote in parsed_quotes:
                quote_text = quote.span.text
                author_name = quote.small.text
                quote_id = Quote.objects.get(quote_text=quote_text)
                # check if the quote already exist in the database
                if not quote_id:
                    # save author using get_or_create
                    r2 = requests.get(base_url+quote.a.get('href'))
                    soup2 = BeautifulSoup(r2.content, 'html.parser')
                    author_description = soup2.find('div', {'class': 'author-description'}).text
                    obj, created = Author.objects.get_or_create(
                        author_name=author_name,
                        defaults={'author_description': author_description},
                    )
                    # save the quote
                    author_id = Author.objects.get(author_name=author_name)
                    q = Quote.objects.create(quote_text=quote_text, authors_id=author_id)
                    counter += 1
        # go to next page or break if this is the last page
        r = requests.get(base_url + next_button_url)
        soup = BeautifulSoup(r.content, 'html.parser')
        next_button_url = soup.find('li', {'class': 'next'}).a.get('href')
        if not next_button_url:  # so this is the last page
            break
        send_mail(
            'parsing task completed',
            'all quotes have been parsed',
            'sender@abc.com',
            'recepient@abc.com',
            fail_silently=False,
        )
