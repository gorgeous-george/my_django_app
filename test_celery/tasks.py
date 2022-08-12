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
    url = base_url
    counter = 0  # counter to stop the loop after 5 quotes saved

    # cycle for pagination to be stopped at the last page
    while True:
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        # take all quotes on the page
        parsed_quotes = soup.find_all('div', {'class': 'quote'})
        # iteration through each quote on the page
        for quote in parsed_quotes:
            # parsing of values
            quote_text = quote.span.text
            author_name = quote.small.text
            quote_exists = Quote.objects.filter(quote_text=quote_text).exists()
            # check if the quote doesn't exist in the database
            if not quote_exists:
                # save author using get_or_create
                r2 = requests.get(base_url+quote.a.get('href'))
                soup2 = BeautifulSoup(r2.content, 'html.parser')
                author_description = soup2.find('div', {'class': 'author-description'}).text
                author, created = Author.objects.get_or_create(
                    author_name=author_name,
                    defaults={'author_description': author_description},
                )
                # save the quote with author_id reference (ForeignKey)
                author_id = Author.objects.get(author_name=author_name).id
                Quote.objects.create(quote_text=quote_text, authors_id=author_id)
                counter += 1
                # to stop the "for quote in parsed_quotes:" after saving of 5 quotes from one page
                if counter == 5:
                    break
        # to stop the "while True:" after saving of 5 quotes in case of saving from different pages
        if counter == 5:
            break
        # update url to parse the next page or break the cycle "while True:" if current page is the last page
        next_button = soup.find('li', {'class': 'next'})
        if next_button:
            next_button_url = soup.find('li', {'class': 'next'}).a.get('href')
            url = base_url + next_button_url
        else:  # so this is the last page
            send_mail(
                'parsing task completed',
                'all quotes have been parsed',
                'sender@abc.com',
                ['recepient@abc.com'],
                fail_silently=False,
            )
            break
