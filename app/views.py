from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView

from .servises import FormList
from .forms import ClientForm
from .models import Client


class HomeList(ListView):
    models = Client
    template_name = 'index.html'
    context_object_name = 'clients'

    def get_queryset(self):
        return Client.objects.all()


class NewClientView(FormList, CreateView):
    form_class = ClientForm
    template_name = 'new_client.html'

    def form_valid(self, form):
        self.user_form_valid(self.request)
        form_client = form.save(commit=False)
        clients = Client.objects.filter(phone=form_client.phone)
        client = clients.first()
        if clients.exists():
            client.price += int(form_client.price)
            if not client.first_name and form_client.first_name:
                client.first_name = form_client.first_name
            if not client.last_name and form_client.last_name:
                client.last_name = form_client.last_name
            client.count += 1
            client.save()
            return redirect("home")
        return super().form_valid(form)


class RemoveClientView(DeleteView):
    model = Client
    template_name = 'remove_client.html'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'

    def get(self, request, *args, **kwargs):
        # client = Client.objects.get(id=self.get_object().id)
        # client.delete()
        print(1)
        return super().get(request, *args, **kwargs)

