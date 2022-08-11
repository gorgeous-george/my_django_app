from django.db import models


class Author(models.Model):
    author_name = models.CharField(max_length=30)
    author_description = models.TextField()


class Quote(models.Model):
    quote_text = models.CharField(max_length=250)
    authors = models.ForeignKey(Author, on_delete=models.CASCADE)
