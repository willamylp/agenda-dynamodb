from django.shortcuts import render

# Create your views here.
def ListarContatos(request):
    contatos = Hosts.objects.all().values()
    contatos2 = json.loads(json.dumps(list(contatos), cls=DjangoJSONEncoder))
    for i in range(len(contatos2)):
        print("-->>>> Host {}: {}".format(i, contatos2[i]['hostname']))
        print(contatos2[i].values())
    return render(request, 'listagemContatos/ListarContatos.html', {'contatos': contatos})
# Create your views here.