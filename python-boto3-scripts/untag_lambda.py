import boto3
import json
import os
import csv
from botocore.exceptions import ClientError


session = boto3.Session(
        #region_name='us-east-1',
        profile_name='moreretail-infra-cli'
        #profile_name='outlook'
        )

#client = boto3.client('lambda',region_name='ap-south-1')
#response = client.list_functions()

lambda_client = session.client('lambda')
#response = lambda_client.list_functions()
paginator = lambda_client.get_paginator('list_functions')

for page in paginator.paginate():
    for function in page['Functions']:
    #print(function['FunctionName'])
    #print("  Function:", function['FunctionName'])
        response = lambda_client.list_tags(Resource=function['FunctionArn'])
        tags = response['Tags']
        if not tags:
            print(" Lambda Function", function['FunctionName'], "does not have tags")

        elif tags:
            print(" Lambda Function", function['FunctionName'], "does  have tags")
#get Untag lambda  code start
#def get_untag_lambda(lambda_list):
#  for i in range(len(lambda_list['Functions'])):
#     lambda_name = lambda_list['Functions'] [i] ['FunctionName']
#     lambda_ARN  = lambda_list['Functions'] [i] ['FunctionArn']
#     tags={}
#     lambda_abscent_tag={}
#     tags_key_list=[]   
#     response = lambda_client.list_tags(
#      Resource= lambda_ARN ,
#      )
#     tags=response['Tags']   
#     tags_key_list= tags.keys() 
#     no_of_tags=len(tags_key_list) 
#     lambda_abscent_tag["Tags"]= {no_of_tags}
#     print(lambda_name)
#     for i in range(len(tags_keys)):
#        if tags_keys [i] not in tags_key_list:
#            key=tags_keys [i]
#            lambda_abscent_tag["Tags"].update({key})
#            untag_lambda[lambda_name]=lambda_abscent_tag 
#  return untag_lambda
##get Untag lambda  code end

#!/usr/bin/python

#import boto3
#from botocore.exceptions import ClientError
#import requests
#import os.path
## Converts string representation of a dict to a dict
#import ast
#from pdb import set_trace as breakpoint
#
#def getLambdas():
#    lm = boto3.client("lambda")
#    funcs = []
#    kwargs = {}
#    try:
#        while True:
#            lfuncs = lm.list_functions(**kwargs)
#            funcs.extend(lfuncs["Functions"])
#            if "NextMarker" in lfuncs:
#                kwargs["Marker"] = lfuncs["NextMarker"]
#            else:
#                break
#    except botocore.exceptions.ClientError as e:
#        # print(f"not enabled (clienterror): {e}")
#        pass
#    except botocore.exceptions.UnauthorizedOperation as e:
#        # print(f"not enabled (unauthorised): {e}")
#        pass
#    return funcs
