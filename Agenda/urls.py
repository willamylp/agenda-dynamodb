from django.urls import path
from Agenda.views import RegistrarContato, ListarContatos, AtualizarContato, DeletarContato

urlpatterns = [
	path('', ListarContatos, name="ListarContato"),
    #path('', Principal, name="Principal"),
    path('RegistrarContato/', RegistrarContato, name="RegistrarContato"),
    path('AtualizarContato/<int:id>/', AtualizarContato, name="AtualizarContato"),
    path('DeletarContato/<int:id>/', DeletarContato, name="DeletarContato"),
    
]