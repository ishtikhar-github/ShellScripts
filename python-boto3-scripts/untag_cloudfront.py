import boto3
import csv
import json

session = boto3.Session(
        #profile_name='outlook'
        profile_name='default'
        )

cf = session.client('cloudfront')
response = cf.list_distributions()
print('\n')
for cflist in response['DistributionList']['Items']:
      cfid = cflist['Id']
      cfarn = cflist['ARN']
      #print(cfid,'\n',cfarn)
      cf_tags = cf.list_tags_for_resource(Resource=cfarn)
      #print(cf_tags)
      tagresponse = cf_tags['Tags']['Items']
      #print(tagresponse)
      if tagresponse == []:
       print(f"The cloudfront {cfid} does not have any Tags")

      #elif tagresponse != []:
      # print(f"The cloudfront {cfid} does have Tags {tagresponse}")
 
