from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from .servises import FormList
from .forms import ClientForm
from .models import Client


class HomeList(ListView):
    models = Client
    template_name = 'index.html'
    context_object_name = 'clients'

    def get_queryset(self):
        return Client.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['home'] = True
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

    # def form_valid(self, form):
    #     return super().user_form_valid(self.request, self.get_context_data, form)


class RemoveClientView(DeleteView):
    model = Client
    template_name = 'remove_client.html'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'
