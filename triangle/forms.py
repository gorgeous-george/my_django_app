from django import forms


class GetForm(forms.Form):
    cat_first = forms.IntegerField(label="first cat", min_value=1, required=True)
    cat_second = forms.IntegerField(label="second cat", min_value=1, required=True)
