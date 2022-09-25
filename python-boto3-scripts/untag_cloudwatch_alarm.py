import boto3
import csv
import json
import logging
import botocore
from botocore.exceptions import ClientError

#AWS_REGION = "us-east-1"
#sqs_client = boto3.client("sqs", region_name=AWS_REGION)

session = boto3.Session(
        #profile_name='outlook'
        profile_name='moreretail-infra-cli'
        )

cw = boto3.client('cloudwatch')
#response = cw.describe_alarms()
paginator = cw.get_paginator('describe_alarms')
#print(response)
#for alarm_name in response['MetricAlarms']:
for page in paginator.paginate():
    for alarm in page['MetricAlarms']:
      alarmname = alarm['AlarmName']
      alarmarn = alarm['AlarmArn']
      #print(alarm['AlarmName'])

        
      #alarmname=alarm_name['AlarmName']
      #alarmarn=alarm_name['AlarmArn']
      #print(alarmname,'\n',alarmarn)
      tagresponse = cw.list_tags_for_resource(ResourceARN=alarmarn)
      #print(tagresponse['Tags'])
      if tagresponse['Tags'] == []:
          print("the cloudwatch alarm",alarmname,"does not have any tags")
      #elif tagresponse['Tags'] != []:
      #    print("the cloudwatch alarm",alarmname,"does have tags")
