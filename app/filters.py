import django_filters as filter
from django_filters import DateFilter

from app.models import Client


class ClientFilter(filter.FilterSet):
    start_data = DateFilter(field_name='updated', lookup_expr='gte')
    end_data = DateFilter(field_name='updated', lookup_expr='lte')

    class Meta:
        model = Client
        fields = ('first_name', 'last_name', 'phone', 'price', 'count', 'black_list')
        exclude = ('addition', 'updated')

