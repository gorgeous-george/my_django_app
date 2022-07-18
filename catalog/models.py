from django.db import models


class City(models.Model):
    city = models.fields.CharField(max_length=30)

    def __str__(self):
        return self.city


class Client(models.Model):
    name = models.fields.CharField(max_length=30)
    phone_number = models.fields.IntegerField()
    product = models.ManyToManyField('Product')
    city = models.ForeignKey('City', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Product(models.Model):
    product_choices = [
        ('3_hours', '3 hours trip'),
        ('day', 'full-day trip with lunch break'),
        ('weekend', '2 days trip with camping'),
    ]
    product = models.fields.CharField(max_length=30, choices=product_choices)

    def __str__(self):
        return self.product


class Supplier(models.Model):
    supplier = models.fields.CharField(max_length=30)
    city = models.OneToOneField('City', on_delete=models.CASCADE)
