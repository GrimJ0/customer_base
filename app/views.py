from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView
from django_filters.views import FilterView
from django_tables2 import SingleTableView

from .filters import ClientFilter
from .tables import ClientTable
from .servises import FormList
from .forms import ClientForm
from .models import Client


class HomeList(SingleTableView, FilterView):
    models = Client
    filterset_class = ClientFilter
    table_class = ClientTable
    paginate_by = 9
    template_name = 'index.html'
    context_object_name = 'clients'

    def get_queryset(self):
        queryset = Client.objects.all()
        client_filtered_list = ClientFilter(self.request.GET, queryset=queryset)
        return client_filtered_list.qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['home'] = True
        context['client_filter'] = ClientFilter(self.request.GET, queryset=self.get_queryset())
        return context


class NewClientView(FormList, CreateView):
    form_class = ClientForm
    template_name = 'new_client.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['new_client'] = True
        return context

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


class EditRecipeView(UpdateView):
    """Класс для редактирования рецепта"""
    model = Client
    form_class = ClientForm
    template_name = 'new_client.html'
    pk_url_kwarg = 'id'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['edit'] = True
        return context


class RemoveClientView(DeleteView):
    model = Client
    template_name = 'remove_client.html'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'
