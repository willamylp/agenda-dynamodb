from django.shortcuts import get_object_or_404, redirect, render
from urllib import request
from django.contrib import messages
from .models import Contatos
from .forms import AgendaForm
from Agenda import urls

def RegistrarContato(request):
    form = AgendaForm(request.POST or None)
    if(form.is_valid()):
        form.save()
        messages.success(request, 'Contato Registrado com Sucesso!')
        print(form)
        return redirect('/')
    return render(request, './formContato.html', {'form': form})

# Create your views here.
def ListarContatos(request):
    contatos = Contatos.objects.all()
    '''contatos2 = json.loads(json.dumps(list(contatos), cls=DjangoJSONEncoder))
    for i in range(len(contatos2)):
        print("-->>>> Contato {}: {}".format(i, contatos2[i]['nome']))
        print(contatos2[i].values())'''
    return render(request, './listarContatos.html', {'contatos': contatos})
# Create your views here.

def AtualizarContato(request, id):
    contato = get_object_or_404(Contatos, pk=id)
    form = AgendaForm(request.POST or None, instance=contato)
    if(form.is_valid()):
        form.save()
        return redirect('/')
    return render(request, './formContato.html', {'form': form})

def DeletarContato(request, id):
    contatoDelete = get_object_or_404(Contatos, pk=id)
    contatoDelete.delete()
    return redirect('/')
