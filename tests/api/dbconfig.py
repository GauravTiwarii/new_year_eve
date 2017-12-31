from __future__ import unicode_literals, print_function
import boto3
import os
import uuid
from moto import mock_dynamodb2


def init():
    ''' Creates the databases and returns the client
    and the table '''

    os.environ['AWS_DEFAULT_REGION'] = 'ap-south-1'
    dynamodb = boto3.resource('dynamodb',  region_name = 'ap-south-1')
    table_name = os.getenv('PROJECT_TABLE', 'new_year_eve')
    # active_tables = dynamodb.list_tables()['TableNames']
    # table = dynamodb.Table(table_name)
    # table.delete()
    # if table_name in active_tables:
    table = dynamodb.create_table(
        TableName = table_name,
        KeySchema = [
            {
                'AttributeName' : 'activity_id',
                'KeyType' : 'HASH' #Partition key
            }
        ],
        AttributeDefinitions = [{
            'AttributeName' : 'activity_id',
            'AttributeType' : 'S'
            }
        ],
        ProvisionedThroughput = {
            'ReadCapacityUnits' : 10,
            'WriteCapacityUnits' : 10
        }
    )
    #Wait, until the table exists
    table.meta.client.get_waiter('table_exists').wait(TableName = table_name)
    assert table.table_status == 'ACTIVE'


    items = [
             {'activity_id' :  str(uuid.uuid4()), 'title' : 'Drop the Ball @NEWYORK'},
             {'activity_id' :  str(uuid.uuid4()), 'title' : 'Cry like a Baby, because you are a loner.'},
             {'activity_id' :  str(uuid.uuid4()), 'title' : 'Wasabi, try to get a LIFE.'},
             {'activity_id' :  str(uuid.uuid4()), 'title' : 'hola, papi!!!'}
            ]
    for item in items :
        table.put_item(Item = item)

    # else:
    #     table = dynamodb.Table(table_name)
    #

    return dynamodb, table
