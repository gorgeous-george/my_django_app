from aggregation.models import Author, Book, Publisher, Store

from django.contrib import admin


class BookInline(admin.TabularInline):
    model = Book
    extra = 0


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'age')
    list_filter = ['name', 'age']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    date_hierarchy = 'pubdate'
    list_display = ('name', 'pages', 'price', 'pubdate', 'rating')
    list_filter = ['name', 'pages', 'price', 'pubdate', 'rating']
    search_fields = ['name']
    search_help_text = 'put the name of the book'


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    inlines = [BookInline]


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    pass
