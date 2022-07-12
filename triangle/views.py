from math import sqrt

from django.shortcuts import render

from triangle.forms import GetForm


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
