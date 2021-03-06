import os
import json
import uuid
import datetime
import boto3
from boto3.dynamodb.conditions import Key
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event, context):
    ''' The get Handler'''
    table_name = os.getenv('PROJECT_TABLE', 'new_year_eve')
    region_name = ('AWS_REGION' , 'ap-south-1')
    client = boto3.resource('dynamodb', region_name = region_name)

    result = get_new_year_eve_options(client, table_name)
    return respond(None, result)



def get_new_year_eve_options(client, table_name):
    '''client is the dynamodb client
        table_name is the name of the dynamodb where records
        are stored.'''

    table = client.Table(table_name)
    result = table.scan()
    return result['Items']
