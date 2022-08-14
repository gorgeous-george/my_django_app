from aggregation.views import \
    BookCreate, \
    BookDelete, \
    BookUpdate, \
    BookListView, \
    BookDetailView, \
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
    path('book_detail/<pk>/', BookDetailView.as_view(), name="book_detail"),
    path('book_list_view/', BookListView.as_view(), name="book_list_view"),
    path('book_create/', BookCreate.as_view(), name="book_create"),
    path('book_update/<pk>', BookUpdate.as_view(), name="book_update"),
    path('book_delete/<pk>', BookDelete.as_view(), name="book_delete"),
    path('books/details/', book_details, name="book_details"),
    path('publishers/', publisher, name="publisher"),
    path('publishers/details/', publisher_details, name="publisher_details"),
    path('stores/', store, name="store"),
    path('stores/details/', store_details, name="store_details"),
]
