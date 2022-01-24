import django_filters as filter
from django.forms import DateInput, CheckboxInput
from django_filters import DateFilter, NumberFilter, BooleanFilter

from app.models import Client


class ClientFilter(filter.FilterSet):
    start_data = DateFilter(field_name='updated', lookup_expr='gte', widget=DateInput(
        attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'Дата начала'}))

    end_data = DateFilter(field_name='updated', lookup_expr='lte', widget=DateInput(
        attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'Дата конеца'}))

    price_min = NumberFilter(field_name='price', lookup_expr='gte')
    price_max = NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Client
        fields = ('first_name', 'last_name', 'phone', 'price', 'count', 'black_list')
        exclude = ('addition', 'updated')
