#it should get a list of options available for new_year_eve.
#the total length should be 4
#
from __future__ import unicode_literals, print_function
from __future__ import absolute_import

import os
import sys

import boto3
import sys
import os
import uuid
import json
from os.path import dirname, join
from moto import mock_dynamodb2


from api.get_new_year_eve_options import get_new_year_eve_options
from dbconfig import init



class Test_get_new_year_eve_options(object):
    @mock_dynamodb2
    def test_total_length_of_provided_content(self):
        client, table = init()
        new_year_eve_options = get_new_year_eve_options(client, table.table_name)

        assert len(new_year_eve_options) == 4

    @mock_dynamodb2
    def test_provided_options(self):
        client, table = init()
        new_year_eve_options = get_new_year_eve_options(client, table.table_name)

        assert new_year_eve_options[0]['title'] == 'Drop the Ball @NEWYORK'

        for option in new_year_eve_options :
            assert 'title' in option
            assert 'activity_id' in option


    @mock_dynamodb2
    def test_get_new_year_eve_options_handler(event, context):
        client, table = init()

        results = handler(event, {})

        assert results
        assert 'statusCode' in results and results['statusCode'] == '200'
        assert 'body' in results
