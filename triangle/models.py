from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return self.first_name


class HistoryLog(models.Model):
    path = models.CharField(max_length=30)
    method = models.CharField(max_length=100, choices=[('get', 'GET request'), ('post', 'POST request')])
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.timestamp
