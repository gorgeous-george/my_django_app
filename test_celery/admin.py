from django.contrib import admin

from test_celery.models import Author, Quote


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
