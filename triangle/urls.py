from django.urls import path

from triangle.views import create_form, index, update_form


app_name = "triangle"

urlpatterns = [
    path('', index, name="index"),
    path('person/', create_form, name="create-form"),
    path('person/<int:pk>/', update_form, name="update-form"),
]
