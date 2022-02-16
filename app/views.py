from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import ClienteModelForm
from django.views.generic import TemplateView, FormView, ListView
from .models import Cliente, Servico
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Create your views here.
class InicioView(TemplateView):
    template_name = 'inicio.html'


class ClientesView(ListView):
    template_name = 'clientes.html'
    model = Cliente
    queryset = Cliente.objects.all()
    context_object_name = 'clientes'


class CreateClienteView(CreateView):
    template_name = 'form_cliente.html'
    model = Cliente
    fields = ['nome', 'telefone', 'dataNascimento', 'imagem']
    success_url = reverse_lazy('clientes')


class UpdateClienteView(UpdateView):
    template_name = 'form_cliente.html'
    model = Cliente
    fields = ['nome', 'telefone', 'dataNascimento', 'imagem']
    success_url = reverse_lazy('clientes')


class ServicosView(TemplateView):
    template_name = 'servicos.html'

    def get_context_data(self, **kwargs):
        context = super(ServicosView, self).get_context_data(**kwargs)
        context['servicos'] = Servico.objects.all()
        return context
