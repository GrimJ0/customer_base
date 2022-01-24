from django import forms

from .models import Client


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ["first_name", "last_name", "phone", "price"]
        widgets = {
            'first_name': forms.TextInput(
                attrs={'class': 'form-control first_name', 'placeholder': 'First name', 'id': 'validationCustom1',
                       'aria-label': 'First name'}),
            'last_name': forms.TextInput(
                attrs={'class': 'form-control last_name', 'placeholder': 'Last name', 'id': 'validationCustom2',
                       'aria-label': 'Last name'}),
            'phone': forms.TextInput(
                attrs={'class': 'form-control phone', 'placeholder': 'phone', 'id': 'validationCustom3',
                       'aria-label': 'phone', 'value': '+7'}),
            'price': forms.TextInput(
                attrs={'class': 'form-control price', 'placeholder': 'price', 'id': 'validationCustom4',
                       'aria-label': 'price', 'min': '0'})
        }
