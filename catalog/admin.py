from django.contrib import admin
from catalog.models import Client, Product, City, Supplier

admin.site.register(Client)
admin.site.register(Product)
admin.site.register(City)
admin.site.register(Supplier)
