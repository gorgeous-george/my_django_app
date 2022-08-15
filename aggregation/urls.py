from aggregation.views import (
    BookCreate,
    BookDelete,
    BookDetailView,
    BookListView,
    BookUpdate,
    author,
    author_details,
    book,
    book_details,
    index,
    publisher,
    publisher_details,
    store,
    store_details,
    )

from django.urls import path
from django.views.generic import TemplateView

app_name = "aggregation"

urlpatterns = [
    path('', index, name="index"),
    path('authors/', author, name="author"),
    path('authors/details/', author_details, name="author_details"),
    path('books/', book, name="book"),
    path('book_detail/<int:pk>/', BookDetailView.as_view(), name="book_detail"),
    path('book_list_view/', BookListView.as_view(), name="book_list_view"),
    path('book_create/', BookCreate.as_view(), name="book_create"),
    path('book_update/<int:pk>', BookUpdate.as_view(template_name="aggregation/book_update.html"), name="book_update"),
    path('book_delete/<int:pk>', BookDelete.as_view(), name="book_delete"),
    path('books/details/', book_details, name="book_details"),
    path('cbv_index/', TemplateView.as_view(template_name="aggregation/cbv_index.html"), name="cbv_index"),
    path('publishers/', publisher, name="publisher"),
    path('publishers/details/', publisher_details, name="publisher_details"),
    path('stores/', store, name="store"),
    path('stores/details/', store_details, name="store_details"),
    path('success/', TemplateView.as_view(template_name="aggregation/success.html"), name="success"),
]
