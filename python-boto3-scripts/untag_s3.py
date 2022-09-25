#import boto3
#from botocore.exceptions import ClientError
#s3_client = boto3.client('s3')
#dict_of_s3_buckets = s3_client.list_buckets()
#list_of_s3_buckets= [each['Name'] for each in dict_of_s3_buckets['Buckets']]
#i=0
#s3_bucket_tag_status={}
#while i<len(list_of_s3_buckets):
#    s3_bucket_name = list_of_s3_buckets[i]
#    try:
#        response = s3_client.get_bucket_tagging(Bucket=s3_bucket_name)
#        tags = response['TagSet']
#        s3_bucket_tag_status[s3_bucket_name]=tags
#    except ClientError:
#        print(s3_bucket_name, "does not have tags")
#        no_tags='does not have tags'
#        s3_bucket_tag_status[s3_bucket_name]=no_tags
#    i+=1


# Find Untagged S3 Bucket
import boto3
from botocore.exceptions import ClientError
session = boto3.Session(
        #region_name='ap-south-1',
        #profile_name='outlook'
        profile_name='moreretail-infra-cli'
        )
s3_client = session.client('s3')
dict_of_s3_buckets = s3_client.list_buckets()
list_of_s3_buckets= [each['Name'] for each in dict_of_s3_buckets['Buckets']]
i=0
s3_bucket_tag_status={}
while i<len(list_of_s3_buckets):
    s3_bucket_name = list_of_s3_buckets[i]
    try:
        response = s3_client.get_bucket_tagging(Bucket=s3_bucket_name)
        tags = response['TagSet']
        s3_bucket_tag_status[s3_bucket_name]=tags
    except ClientError:
        print("S3 Bucket",s3_bucket_name, "does not have tags")
        no_tags='does not have tags'
        s3_bucket_tag_status[s3_bucket_name]=no_tags
    i+=1


