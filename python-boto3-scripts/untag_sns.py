import boto3
import csv
import json

session = boto3.Session(
        #profile_name='outlook'
        profile_name='moreretail-infra-cli'
        )

sns = session.client('sns')
response = sns.list_topics()
list_arn_name = []
for topic in response['Topics']:
    topic_name = topic['TopicArn'].rsplit(':',1)[1]
    topicarn = topic['TopicArn']
   #list_arn_name.append(topic['TopicArn'].split(':'))
   #for each in list_arn_name:
       #print(each[5])
    tagresponse = sns.list_tags_for_resource(ResourceArn=topicarn)
    if tagresponse['Tags'] == []:
           print(f"The Topic {topic_name} does not have tags")
 
    #if tagresponse['Tags'] != []:
    #elif tagresponse['Tags'] != []:
    #       print(f"The Topic {topic_name} does have tags {tagresponse['Tags']}")


#import boto3
#from pprint import pprint
#
#account_id = input("Enter the AWS account Id:")
#regions = ['ap-northeast-1', 'ap-southeast-1',
#       'ca-central-1', 'us-east-1', 'us-east-2']
#
#list_arn_name = []
#
#for region in regions:
#    session = boto3.session.Session()
#    client = session.client('sns', region_name=region)
#    for arn in client.list_topics()['Topics']:
#        list_arn_name.append(arn['TopicArn'].split(':'))
#        for each in list_arn_name:
#            print(each[5])
#
