#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals
import boto3
import json

def lambda_handler(event, context):
    clean_old_lambda_versions()
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('All Lambda Deleteed !!!')
    }
    
def clean_old_lambda_versions(marker=''):
    client = boto3.client('lambda')
    if marker == '':
        functions = client.list_functions()
    else:
        functions = client.list_functions(Marker=marker)
    for function in functions['Functions']:
        while True:
            versions = \
                client.list_versions_by_function(FunctionName=function['FunctionArn'
                    ])['Versions']
            if len(versions) == 1:
                print('{}: done'.format(function['FunctionName']))
                print(function['FunctionName'])
                if(function['FunctionName'] != 'python-delete-all-lambda'):
                    client.delete_function(FunctionName=function['FunctionName'
                        ])
                break
    if 'NextMarker' in functions:
        clean_old_lambda_versions(functions['NextMarker'])
    

