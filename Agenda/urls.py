from django.urls import path
from Agenda.views import Principal, RegistrarContato, ListarContatos

urlpatterns = [
    path('', Principal, name="Principal"),
    path('RegistrarContato/', RegistrarContato, name="RegistrarContato"),
    path('ListarContatos/', ListarContatos, name="ListarContato"),
]