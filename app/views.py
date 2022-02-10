from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import ClienteModelForm
from django.views.generic import TemplateView, FormView
from .models import Cliente, Servico
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Create your views here.
class InicioView(TemplateView):
    template_name = 'inicio.html'


class ClientesView(CreateView):
    template_name = 'clientes.html'
    model = Cliente
    fields = ['nome', 'telefone', 'dataNascimento', 'imagem']
    success_url = reverse_lazy('clientes')

    def get_context_data(self, **kwargs):
        context = super(ClientesView, self).get_context_data(**kwargs)
        context['clientes'] = Cliente.objects.all()
        return context


class ServicosView(TemplateView):
    template_name = 'servicos.html'

    def get_context_data(self, **kwargs):
        context = super(ServicosView, self).get_context_data(**kwargs)
        context['servicos'] = Servico.objects.all()
        return context
