from math import sqrt

from django.shortcuts import get_object_or_404, redirect, render

from triangle.forms import GetForm, MyModelForm
from triangle.models import Person


def index(request):
    gip = None
    if "submit" in request.GET:
        get_form = GetForm(request.GET)
        if get_form.is_valid():
            gip = sqrt(get_form.cleaned_data["cat_first"] ** 2 + get_form.cleaned_data["cat_second"] ** 2)
    else:
        get_form = GetForm()
    return render(
        request,
        "triangle/index.html",
        {
            "get_form": get_form,
            "gip": gip
        }
    )


def create_form(request):
    title_text = "Create new instance"
    if request.method == 'POST':
        form = MyModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('triangle:create-form')
    else:
        form = MyModelForm()
    return render(
        request,
        "triangle/create_form.html",
        {
            "form": form,
            "title_text": title_text,

        }
    )


def update_form(request, pk):
    obj = get_object_or_404(Person, id=pk)
    title_text = "Update instance with id"
    if request.method == 'POST':
        form = MyModelForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("triangle:update-form", pk)
    else:
        form = MyModelForm(instance=obj)
    return render(
        request,
        "triangle/update_form.html",
        {
            "form": form,
            "title_text": title_text,
            "obj": obj,

        }
    )
