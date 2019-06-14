import boto3

dynamodb = boto3.resource('dynamodb')
dynamoTable = dynamodb.Table('agenda')


def InsertInto(dynamoTable):
    dynamoTable.put_item(
        Item = {
            'id': 2,
            'Nome': 'Willamy',
            'Telefone': '(84) 9 9669-2906',
            'E-mail': 'willamy.wlp@gmail.com'
        }
    )

def DeleteItem(dynamoTable, key):
    


InsertInto(dynamoTable)

