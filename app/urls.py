from django.urls import path
from .views import InicioView, ClientesView, ServicosView, UpdateClienteView, CreateClienteView

urlpatterns = [
    path('', InicioView.as_view(), name='inicio'),
    path('clientes/', ClientesView.as_view(), name='clientes'),
    path('servicos/', ServicosView.as_view(), name='servicos'),
    path('update/<int:pk>/', UpdateClienteView.as_view(), name='update_cliente'),
    path('create-cliente/', CreateClienteView.as_view(), name='create_cliente')
]
