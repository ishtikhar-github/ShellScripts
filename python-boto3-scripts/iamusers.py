import boto3
import csv
import json

session = boto3.Session(
        #profile_name='outlook'
        profile_name='default'
        )

iam = session.client('iam')
#iamusers = iam.list_users()
#users = iamusers['Users']
paginator = iam.get_paginator('list_users')

print("IAM UserName")
l = []


#for x in iamusers['Users']:
for page in paginator.paginate():
 for user in page['Users']:
    print (user['UserName']) 

