from django.urls import path
from .views import InicioView, ClientesView, ServicosView

urlpatterns = [
    path('', InicioView.as_view(), name='inicio'),
    path('clientes/', ClientesView.as_view(), name='clientes'),
    path('servicos/', ServicosView.as_view(), name='servicos'),
]
