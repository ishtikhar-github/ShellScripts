import boto3
import csv
import json
import logging
import botocore
from botocore.exceptions import ClientError

#AWS_REGION = "us-east-1"
#sqs_client = boto3.client("sqs", region_name=AWS_REGION)

#session = boto3.Session(
#        #profile_name='outlook'
#        profile_name='moreretail-infra-cli'
#          )

session = boto3.Session(
        region_name='ap-south-1',
        #profile_name='outlook'
        profile_name='moreretail-infra-cli'
        )

cw = boto3.client('logs')
paginator = cw.get_paginator('describe_log_groups')

#response = cw.describe_log_groups()
#print(response)
for page in paginator.paginate():
 for lg in page['logGroups']:
      lgname=lg['logGroupName']
      lgarn=lg['arn']
      #print(lgname,lgarn)
      tagresponse = cw.list_tags_log_group(logGroupName=lgname)
      #print(tagresponse['tags'])
      tags = tagresponse['tags']
      if tagresponse['tags'] == {}:
          print("the cloudwatch log group",lgname,"does not have any tags")
      #elif tagresponse['tags'] != {}:
      #    print("the cloudwatch log group ",lgname,"does have tags",tags)
