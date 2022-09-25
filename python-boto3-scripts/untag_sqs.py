import boto3
import csv
import json
import logging
import botocore
from botocore.exceptions import ClientError

#AWS_REGION = "us-east-1"
#sqs_client = boto3.client("sqs", region_name=AWS_REGION)

session = boto3.Session(
        profile_name='moreretail-infra-cli'
        )

sqs = boto3.client('sqs')
response = sqs.list_queues()
for queue in response['QueueUrls']:
    queueurl = queue
    queuename = queue.rsplit('/',1)[1]
    #print(queuename)
    try:
        tagresponse = sqs.list_queue_tags(QueueUrl=queueurl)
        tags = tagresponse['Tags']
    except KeyError:
        print(f" SQS Queue {queuename} does not have any tags")


