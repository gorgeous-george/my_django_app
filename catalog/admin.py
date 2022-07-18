from django.contrib import admin

from catalog.models import City, Client, Product, Supplier

admin.site.register(Client)
admin.site.register(Product)
admin.site.register(City)
admin.site.register(Supplier)
