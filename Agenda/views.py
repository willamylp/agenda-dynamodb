from django.shortcuts import get_object_or_404, redirect, render
from urllib import request
from django.contrib import messages
from .models import Contatos
from .forms import AgendaForm
from Agenda import urls
import json
import boto3
from django.core.serializers.json import DjangoJSONEncoder

def GetDynamoTable():
    dynamodb = boto3.resource('dynamodb')
    dynamoTable = dynamodb.Table('agenda')
    return dynamoTable

def InsertIntoDynamoDB(contentJSON):
    dynamoTable = GetDynamoTable()
    dynamoTable.put_item(
        Item = {
            'id': contentJSON[-1]['id'],
            'Nome': contentJSON[-1]['nome'],
            'Telefone': contentJSON[-1]['telefone'],
            'Email': contentJSON[-1]['email']
        }
    )

def GetItemDynamoDB(id):
    dynamoTable = GetDynamoTable()
    return dynamoTable.get_item(
        Key = {'id': id}
    )

def UpdateItemDynamoDB(id):
    dynamoTable = GetDynamoTable()
    dynamoTable.update_item(
        Key = {
            'id': id
        },
        UpdateExpression = 'SET Nome = :Nome, Telefone = :Telefone',
        ExpressionAttributeValues = {
            ':Nome': 'Willamy D O Joventino',
            ':Telefone': '(84)9 9669-2906'
        }
    )

def DeleteItemDynamoDB(id):
    dynamoTable = GetDynamoTable()
    dynamoTable.delete_item(
        Key = {'id': id}
    )

# -------------------------------------------------------- #
def ConvertDataJSON(Table):
    dados = Table.objects.all().values()
    contentJSON = json.loads(json.dumps(list(dados), cls=DjangoJSONEncoder))
    return contentJSON

def RegistrarContato(request):
    form = AgendaForm(request.POST or None)
    if(form.is_valid()):
        form.save()
        messages.success(request, 'Contato Registrado com Sucesso!')
        InsertIntoDynamoDB(ConvertDataJSON(Contatos))
        return redirect('/')
    return render(request, './formContato.html', {'form': form})

def ListarContatos(request):
    contatos = Contatos.objects.all()
    #conteudo = dict(Contatos.objects.filter(id=11).values()[0])
    #print(conteudo['email'])
    #print(dict(contatos.values()[0]))
    return render(request, './listarContatos.html', {'contatos': contatos})

def AtualizarContato(request, id):
    contato = get_object_or_404(Contatos, pk=id)
    form = AgendaForm(request.POST or None, instance=contato)
    if(form.is_valid()):
        form.save()
        InsertIntoDynamoDB(ConvertDataJSON(Contatos))
        return redirect('/')
    return render(request, './formContato.html', {'form': form})

def DeletarContato(request, id):
    contatoDelete = get_object_or_404(Contatos, pk=id)
    contatoDelete.delete()
    DeleteItemDynamoDB(id)
    return redirect('/')
