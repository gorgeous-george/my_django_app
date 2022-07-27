from aggregation.views import \
    author, \
    author_details, \
    book, \
    book_details, \
    index, \
    publisher, \
    publisher_details, \
    store, \
    store_details

from django.urls import path

app_name = "aggregation"

urlpatterns = [
    path('', index, name="index"),
    path('authors/', author, name="author"),
    path('authors/details/', author_details, name="author_details"),
    path('books/', book, name="book"),
    path('books/details/', book_details, name="book_details"),
    path('publishers/', publisher, name="publisher"),
    path('publishers/details/', publisher_details, name="publisher_details"),
    path('stores/', store, name="store"),
    path('stores/details/', store_details, name="store_details"),
]
