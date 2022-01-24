from django import forms

from .models import Client


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ["first_name", "last_name", "phone", "price", "black_list"]
        widgets = {
            'first_name': forms.TextInput(
                attrs={'class': 'form-control first_name', 'placeholder': 'Имя', 'id': 'validationCustom1',
                       'aria-label': 'First name'}),
            'last_name': forms.TextInput(
                attrs={'class': 'form-control last_name', 'placeholder': 'Фамилия', 'id': 'validationCustom2',
                       'aria-label': 'Last name'}),
            'phone': forms.TextInput(
                attrs={'class': 'form-control phone', 'placeholder': 'Телефон', 'id': 'validationCustom3',
                       'aria-label': 'phone', 'value': '+7'}),
            'price': forms.TextInput(
                attrs={'class': 'form-control price', 'placeholder': 'Прайс', 'id': 'validationCustom4',
                       'aria-label': 'price'}),
            'black_list': forms.CheckboxInput(
                attrs={'class': 'form-check-input black_list', 'id': 'flexCheckDefault', 'role': 'switch'})
        }
