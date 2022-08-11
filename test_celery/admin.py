from test_celery.models import Author, Quote

from django.contrib import admin


class QuoteInline(admin.TabularInline):
    model = Quote
    extra = 0


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_filter = ['author_name']
    inlines = [QuoteInline]


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    pass
