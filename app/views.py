from django.views.generic import ListView, CreateView

from .forms import ClientForm
from .models import Client


class HomeList(ListView):
    models = Client
    template_name = 'index.html'
    context_object_name = 'clients'

    def get_queryset(self):
        return Client.objects.all()


class NewClientView(CreateView):
    form_class = ClientForm
    template_name = 'new_client.html'
