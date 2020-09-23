from __future__ import absolute_import, print_function, unicode_literals
import boto3


def clean_old_lambda_versions(marker = ''):
    client = boto3.client('lambda',
        region_name='us-east-1',
        aws_access_key_id='<aws_access_key_id>',
        aws_secret_access_key='<aws_secret_access_key>')	
    if marker == '':
    	functions = client.list_functions()
    else:
	functions = client.list_functions(Marker=marker)			
    for function in functions['Functions']:
        while True:
            versions = client.list_versions_by_function(FunctionName=function['FunctionArn'])['Versions']
            if len(versions) == 1:
                print('{}: done'.format(function['FunctionName']))
                print(function['FunctionName'])
                client.delete_function(FunctionName=function['FunctionName'])
                break
    if 'NextMarker' in functions:
		clean_old_lambda_versions(functions['NextMarker'])  
        

if __name__ == '__main__':
    clean_old_lambda_versions()
