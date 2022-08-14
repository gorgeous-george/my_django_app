from django.urls import reverse_lazy

from aggregation.models import Author, Book, Publisher, Store

from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Count, Max, Min, Prefetch, Q, Sum
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.utils.decorators import method_decorator


def index(request):
    return render(
        request,
        "aggregation/index.html",
    )


def author(request):
    books_authors = Book.objects.prefetch_related('authors').order_by('name')
    return render(
        request,
        "aggregation/author.html",
        {
           'books_authors': books_authors,
        }
    )


def author_details(request):
    age = Author.objects.aggregate(Sum('age'), Max('age'), Min('age'), Avg('age'))
    return render(
        request,
        "aggregation/author_details.html",
        {
            'age': age
        }
    )


def book(request):
    publishers_books = Book.objects.select_related('publisher').order_by('pubdate')
    return render(
        request,
        "aggregation/book.html",
        {
            'publishers_books': publishers_books
        }
    )


def book_details(request):
    number_1993 = Book.objects.filter(pubdate='1993-01-01').count()
    return render(
        request,
        "aggregation/book_details.html",
        {
            'number_1993': number_1993
        }
    )


def publisher(request):
    publishers_books = Book.objects.select_related('publisher').order_by('publisher__name')
    return render(
        request,
        "aggregation/publisher.html",
        {
            'publishers_books': publishers_books
        }
    )


def publisher_details(request):
    publishers_count = Publisher.objects.annotate(num_books=Count('book')).order_by('-num_books')
    return render(
        request,
        "aggregation/publisher_details.html",
        {
            'publishers_count': publishers_count
        }
    )


def store(request):
    store_books_authors = Store.objects.prefetch_related('books__authors')
    return render(
        request,
        "aggregation/store.html",
        {
            'store_books_authors': store_books_authors
        }
    )


def store_details(request):
    queryset = Book.objects.filter(Q(price__lte=150) & Q(rating__gte=8))
    store_books_authors = Store.objects.prefetch_related(Prefetch('books', queryset))
    return render(
        request,
        "aggregation/store_details.html",
        {
            'store_books_authors': store_books_authors
        }
    )


class BookDetailView(DetailView):
    model = Book


class BookListView(ListView):
    model = Book
    queryset = Book.objects.select_related("publisher")
    paginate_by = 3


@method_decorator(login_required, name='dispatch')
class BookCreate(CreateView):
    model = Book
    queryset = Book.objects.select_related("publisher")
    fields = ['name', 'pages', 'price', 'rating', 'pubdate', 'publisher']
    success_url = 'http://127.0.0.1:8000/aggregation/book_create/'
    initial = {
        'name': 'test name',
        'pages': 123,
        'price': 123,
        'rating': 10,
        'pubdate': '2022-02-02',
    }


@method_decorator(login_required, name='dispatch')
class BookUpdate(UpdateView):
    Model = Book
    queryset = Book.objects.select_related("publisher")
    fields = ['name', 'pages', 'price', 'rating', 'pubdate', 'publisher']
    success_url = 'http://127.0.0.1:8000/aggregation/book_update/10'


@method_decorator(login_required, name='dispatch')
class BookDelete(DeleteView):
    Model = Book
    queryset = Book.objects.select_related("publisher")
    success_url = 'http://127.0.0.1:8000/aggregation/book_delete/7'
