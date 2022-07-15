from django import forms
from django.forms import ModelForm

from triangle.models import Person


class GetForm(forms.Form):
    cat_first = forms.IntegerField(label="first cat", min_value=1, required=True)
    cat_second = forms.IntegerField(label="second cat", min_value=1, required=True)


class MyModelForm(ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'email']
