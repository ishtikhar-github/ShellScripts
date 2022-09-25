import boto3
import csv
import json

session = boto3.Session(
        #profile_name='outlook'
        profile_name='moreretail-infra-cli'
        )

redshift = session.client('redshift')
response = redshift.describe_clusters()
print('\n')

for redshift_cluster in response['Clusters']:
    cluster_name = redshift_cluster['ClusterIdentifier']
    cluster_arn = f"arn:aws:redshift:ap-south-1:174241535978:cluster:{cluster_name}"
    tagresponse = redshift.describe_tags(ResourceName=cluster_arn)['TaggedResources']
    # If no tags, then it's an untagged resource
    if not tagresponse:
        print(f"The redshift cluster {cluster_name} does not have any tags")
    else:
        print(f"The redshift cluster {cluster_name} have tags {tagresponse}")
    #print('DB instance identifier: ' + str(rds_instance['DBInstanceIdentifier']))
    #print('DB instance status: ' + str(rds_instance['DBInstanceStatus']))
    #print('DB instance Engine: ' + str(rds_instance['Engine']))
    #print('DB instance Engine version: ' + str(rds_instance['EngineVersion']))
    #print('DB instance instance class: ' + str(rds_instance['DBInstanceClass']))
    #print('DB instance instance arn: ' + str(rds_instance['DBInstanceArn']))
    #print('\n')

    #tagresponse = rds.list_tags_for_resource(ResourceName=dbarn)
    #if tagresponse['TagList'] == []:
    ##if tagresponse['Tags'] == {}:
    #  print("The DB Instance Identifier",rds_instance['DBInstanceIdentifier'],"does not have any Tags")

    #elif tagresponse['TagList'] != []:
    ##elif tagresponse['Tags'] != {}:
    #  print("The DB Instance Identifier",rds_instance['DBInstanceIdentifier'],"does have tags",tagresponse['TagList'])


