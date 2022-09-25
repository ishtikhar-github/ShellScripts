#Find Untagged Glue Jobs
#import boto3
#import json
#from botocore.exceptions import ClientError
#
#
#session = boto3.Session(
#        region_name='ap-south-1',
#        profile_name='default'
#        #profile_name='outlook'
#        )
#
#glue_client = session.client('glue')
#response = glue_client.get_jobs()
##response = glue_client.list_jobs()
#
#for job in response['Jobs']:
#        print(job)



import boto3
import json
from botocore.exceptions import ClientError

session = boto3.Session(
        region_name='ap-south-1',
        profile_name='default'
        #profile_name='outlook'
        )


glue_client = session.client('glue')
#response = glue_client.get_jobs()
paginator = glue_client.get_paginator('get_jobs')



for page in paginator.paginate():
 for job in page['Jobs']:
   region_name = 'ap-south-1'
   jobname = job['Name']
   jobarn = f"arn:aws:glue:{region_name}:174241535978:job/{jobname}"
   #print("The Glue JobName is",jobname,"its Resource ARN is",jobarn)

   #tagresponse = glue_client.get_tags(ResourceArn=job['ResourceArn'])
   tagresponse = glue_client.get_tags(ResourceArn=jobarn)
   #print(tagresponse)

   #if tagresponse['Tags'] == []:
   if tagresponse['Tags'] == {}:
      print("The Glue Job",jobname,"does not have any Tags")

   #if tagresponse['Tags'] != {}:
   elif tagresponse['Tags'] != {}:
      print("The Glue Job",jobname,"does have Tags",tagresponse['Tags'])



#import boto3
#from botocore.exceptions import ClientError
#
#def get_tags_from_resource(resource_arn):
#   session = boto3.session.Session(region_name='ap-south-1',profile_name='default')
#   glue_client = session.client('glue')
#   try:
#      response = glue_client.get_tags(ResourceArn=resource_arn)
#      print(response)
#      return response
#   except ClientError as e:
#      raise Exception("boto3 client error in get_tags_from_resource: " + e.__str__())
#   except Exception as e:
#      raise Exception("Unexpected error in get_tags_from_resource: " + e.__str__())
#print(add_tags_in_resource("arn:aws:glue:us-east-1:1122225*****88:database/test-db"))
