import boto3
import csv
import json

session = boto3.Session(
        #profile_name='outlook'
        profile_name='default'
        )


elasticache = session.client('elasticache')
#response = elasticache.describe_cache_clusters()
print('\n')

#response = elasticache.describe_replication_groups(ShowCacheNodeInfo=True, MaxRecords=100)
response = elasticache.describe_replication_groups()
#redis = [replication_group['ReplicationGroupId'] for replication_group in response['ReplicationGroups']]
for redis in response['ReplicationGroups']:
    redis_cluster_name = redis['ReplicationGroupId']
    redis_cluster_arn = redis['ARN']
    #print(redis['ReplicationGroupId'])
    #print("ClusterName: {0}\nClusterARN: {1}\n".format(redis_cluster_name,redis_cluster_arn))
    tagresponse = elasticache.list_tags_for_resource(ResourceName=redis_cluster_arn)
    if tagresponse['TagList'] == []:
       print ("The redis cluster",redis_cluster_name,"does not have any tags")


    #elif tagresponse['TagList'] != []:
    #  print("The redis cluster",redis_cluster_name,"does have tags",tagresponse['TagList'])


