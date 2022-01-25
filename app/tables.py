import django_tables2 as tables

from app.models import Client


class ClientTable(tables.Table):
    actions = tables.TemplateColumn(template_name='skeleton/actions.html', orderable=False, verbose_name='Действия')

    class Meta:
        model = Client
        template_name = "django_tables2/bootstrap4.html"
        fields = ('first_name', 'last_name', 'phone', 'price', 'count', 'addition', 'updated')
        attrs = {
            'class': 'table table-hover',
            'th': {'class': 'col text-secondary alert-link'}
        }
