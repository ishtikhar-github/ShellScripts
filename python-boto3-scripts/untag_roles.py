import boto3
import csv
import json

session = boto3.Session(
        #profile_name='outlook'
        #profile_name='default'
        profile_name='moreretail-infra-cli'
        )

iam = session.client('iam')
#roles = iam.list_roles()
paginator = iam.get_paginator('list_roles')

for page in paginator.paginate():
# for user in page['Users']:

    for role in page['Roles']:
        rolename = role['RoleName']
        tagresponse = iam.list_role_tags(RoleName=rolename)
        tags = tagresponse['Tags']
        if tags == []:
            print(f'The Role {rolename} does not have any tags')
        #elif tags != ['Tags']:
        #    print(f'The Role {rolename} does have tags {tags}')
