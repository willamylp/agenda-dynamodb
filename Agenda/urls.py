from django.urls import path
from Agenda.views import Principal, RegistrarContato, ListarContatos

urlpatterns = [
    path('', Principal, name="Principal"),
    path('', RegistrarContato, name="RegistroContato"),
    path('ListarContatos/', ListarContatos, name="ListarContato"),
]