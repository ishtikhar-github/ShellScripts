import boto3
import csv
import json

session = boto3.Session(
        #profile_name='outlook'
        profile_name='moreretail-infra-cli'
        )

ct = session.client('cloudtrail')
response = ct.list_trails()
print('\n')
for ctlist in response['Trails']:
      ctname = ctlist['Name']
      ctarn = ctlist['TrailARN']
      ct_tags = ct.list_tags(ResourceIdList=[ctarn])

      tagresponse = ct_tags['ResourceTagList']
      if tagresponse[0]['TagsList'] == []:
       print(f"The cloudtrail {ctname} does not have any Tags")

      elif tagresponse[0]['TagsList'] != []:
       print(f"The cloudtrail {ctname} does have Tags {tagresponse[0]}")
 

#import boto3
#client = boto3.client('cloudtrail')

#response = client.describe_trails()
#for cloudtrail in response['trailList']:
#    cloudtrail_name = cloudtrail['Name']
#    response = client.list_tags(ResourceIdList = [cloudtrail_name])
#    if response['ResourceTagList'][0]['Tags'] == []:
#        print(cloudtrail_name)
