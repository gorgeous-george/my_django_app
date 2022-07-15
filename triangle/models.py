from django.db import models


class Person(models.Model):
    first_name = models.fields.CharField(max_length=30)
    last_name = models.fields.CharField(max_length=30)
    email = models.fields.EmailField()

    def __str__(self):
        return self.first_name
