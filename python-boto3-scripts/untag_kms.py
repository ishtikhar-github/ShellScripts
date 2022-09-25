import boto3
import csv
import json
import logging
from datetime import date, datetime
from botocore.exceptions import ClientError



session = boto3.Session(
        #profile_name='outlook'
        profile_name='default'
        )

kms = session.client('kms')
#paginator = kms.get_paginator('list_aliases')
paginator = kms.get_paginator('list_keys')
for page in paginator.paginate():
        for keylist in page['Keys']:
        #print(keylist)
            #keyname = keylist['AliasName']
            #print(keyname)
            #keyarn = keylist['AliasArn']
            keyid = keylist['KeyId']
            #print(f"KeyId:{keyid}") 
            tagresponse = kms.list_resource_tags(KeyId=keyid)
            #print(tagresponse)
            tags = tagresponse['Tags']
            if tags == []:
                print(f"The KMS KeyId:{keyid} does not have any tags")
            if tags != []:
                print(f"The KMS KeyId:{keyid} does have  {tags}")
