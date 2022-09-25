import boto3
import csv
import json

session = boto3.Session(
        #profile_name='outlook'
        profile_name='default'
        )

rds = session.client('rds')
response = rds.describe_db_instances()
cluster = rds.describe_db_clusters()
print('\n')

for rds_instance in response['DBInstances']:
    dbarn = rds_instance['DBInstanceArn']
    #print(rds_instance)
    #print('DB instance identifier: ' + str(rds_instance['DBInstanceIdentifier']))
    #print('DB instance status: ' + str(rds_instance['DBInstanceStatus']))
    #print('DB instance Engine: ' + str(rds_instance['Engine']))
    #print('DB instance Engine version: ' + str(rds_instance['EngineVersion']))
    #print('DB instance instance class: ' + str(rds_instance['DBInstanceClass']))
    #print('DB instance instance arn: ' + str(rds_instance['DBInstanceArn']))
    #print('\n')

    tagresponse = rds.list_tags_for_resource(ResourceName=dbarn)
    if tagresponse['TagList'] == []:
    #if tagresponse['Tags'] == {}:
      print("The DB Instance Identifier",rds_instance['DBInstanceIdentifier'],"does not have any Tags")

    #elif tagresponse['TagList'] != []:
    #elif tagresponse['Tags'] != {}:
    #  print("The DB Instance Identifier",rds_instance['DBInstanceIdentifier'],"does have tags",tagresponse['TagList'])

for rds_cluster in cluster['DBClusters']:
     print('DB Cluster Identifier', rds_cluster['DBClusterIdentifier'])
     dbclusterarn = rds_cluster['DBClusterArn']
     print(dbclusterarn)
     
     tagresponse = rds.list_tags_for_resource(ResourceName=dbclusterarn)
     if tagresponse['TagList'] == []:
     #if tagresponse['Tags'] == {}:
      print("The DB Cluster Identifier",rds_cluster['DBClusterIdentifier'],"does not have any Tags")

     #elif tagresponse['TagList'] != []:
     #elif tagresponse['Tags'] != {}:
     # print("The DB Cluster Identifier",rds_cluster['DBClusterIdentifier'],"does have tags",tagresponse['TagList'])


