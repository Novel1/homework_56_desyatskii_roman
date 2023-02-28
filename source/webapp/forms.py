from django import forms


class ProductForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    description = forms.CharField(max_length=3000, required=True)
    image = forms.CharField(max_length=3000, required=True)
    category = forms.CharField(max_length=1000)
    price = forms.DecimalField(max_digits=7, decimal_places=2)
    remainder = forms.IntegerField(min_value=0)
