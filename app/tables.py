import django_tables2 as tables

from app.models import Client



class ClientTable(tables.Table):
    actions = tables.TemplateColumn(template_name='skeleton/actions.html', verbose_name='Действия')
    class Meta:
        model = Client
        template_name = "django_tables2/bootstrap4.html"
        # fields = ('__all__', 'change',)
        attrs = {
            'class': 'table table-hover',
            # 'th': {'class': 'badge bg-primary'}
        }