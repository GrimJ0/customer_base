from django import forms

from .models import Client


class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = ["first_name", "last_name", "phone", "price"]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First name', 'aria-label': 'First name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last name', 'aria-label': 'Last name'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'phone', 'aria-label': 'phone', 'value': '+7'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'price', 'aria-label': 'price', 'min': '0'})
        }