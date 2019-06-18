from django.shortcuts import get_object_or_404, redirect, render
from urllib import request
from django.contrib import messages
from .models import Contatos
from .forms import AgendaForm
from Agenda import urls

def Principal(request):
    return render(request, './principal.html')

def RegistrarContato(request):
    form = AgendaForm(request.POST or None)
    if(form.is_valid()):
        form.save()
        messages.success(request, 'Contato Registrado com Sucesso!')
        return redirect('./ListarContatos/')
    return render(request, 'principal.html', {'form': form})

# Create your views here.
def ListarContatos(request):
    contatos = Contatos.objects.all()
    '''contatos2 = json.loads(json.dumps(list(contatos), cls=DjangoJSONEncoder))
    for i in range(len(contatos2)):
        print("-->>>> Contato {}: {}".format(i, contatos2[i]['nome']))
        print(contatos2[i].values())'''
    return render(request, './principal.html', {'contatos': contatos})
# Create your views here.