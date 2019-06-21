import boto3


def GetDynamoTable():
    dynamodb = boto3.resource('dynamodb')
    dynamoTable = dynamodb.Table('agenda')
    return dynamoTable


def InsertInto():
    dynamoTable = GetDynamoTable()
    dynamoTable.put_item(
        Item = {
            'id': 3,
            'Nome': 'Willamy 3333',
            'Telefone': '(84) 9 9669-2906',
            'E-mail': 'willamy.wlp@gmail.com'
        }
    )

def DeleteItem(dynamoTable, key):
    pass


InsertInto()

