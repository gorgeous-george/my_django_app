from django.urls import path

from triangle.views import index


app_name = "triangle"

urlpatterns = [
    path('', index, name="index"),
]
