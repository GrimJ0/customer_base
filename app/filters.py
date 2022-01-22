import django_filters
from django_filters import DateFilter

from app.models import Client

class ClientFilter(django_filters.FilterSet):

    start_data = DateFilter(field_name='updated', lookup_expr='gte')
    end_data = DateFilter(field_name='updated', lookup_expr='lte')

    class Meta:
        model = Client
        fields = '__all__'
        exclude = ['addition', 'updated']