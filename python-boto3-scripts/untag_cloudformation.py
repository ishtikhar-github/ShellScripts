import boto3
import csv
import json

session = boto3.Session(
        #profile_name='outlook'
        profile_name='moreretail-infra-cli'
        )

cf = session.client('cloudformation')
response = cf.describe_stacks()
print('\n')
for cflist in response['Stacks']:
  cf_name = cflist['StackName']
  cf_tags = cflist['Tags']
  if cf_tags == []:
     #if tagresponse['Tags'] == {}:
    print(f"The cloudformation {cf_name} does not have any Tags")

  #elif cf_tags != []:
  #  print(f"The cloudformation {cf_name} does have Tags {cf_tags}")
 
