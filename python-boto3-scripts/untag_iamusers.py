import boto3
import csv
import json

session = boto3.Session(
        #profile_name='outlook'
        profile_name='moreretail-infra-cli'
        )

iam = session.client('iam')
paginator = iam.get_paginator('list_users')

for page in paginator.paginate():
 for user in page['Users']:
    username = user['UserName']
    #print (username) 
    tagresponse = iam.list_user_tags(UserName=username)
    tags = tagresponse['Tags']
    if tags == []:
      print(f'Iam User {username} does not have any tag')
 
    #elif tags != []:
    #  print(f'Iam User {username} does have tags {tags}')
