import boto3
import csv
import json

session = boto3.Session(
        profile_name='moreretail-infra-cli',
        #profile_name='default',
        region_name='ap-south-1'
        )

volume = session.client('ec2')
#STS_CLIENT = session.client('sts')
#CURRENT_ACCOUNT_ID = STS_CLIENT.get_caller_identity()['Account']


paginator = volume.get_paginator('describe_volumes')

print('\n')
print(f"-------- Untag Volumes ------------")
for page in paginator.paginate():
 for i in page['Volumes']:
    volumeid = i['VolumeId']
    try:
      tags = i['Tags']
    except KeyError:
      print(f'VolumeId {volumeid} does not have any tags')


print('\n')
print(f"-------- Untag Snapshots ------------")

snapshot = session.client('ec2')
paginator = snapshot.get_paginator('describe_snapshots')
for page in paginator.paginate(OwnerIds=['174241535978']):
    for i in page['Snapshots']:
        snapshotid = i['SnapshotId']
        try:
            tags = i['Tags']
        except KeyError:
            print(f"The SnapshotId {snapshotid} does not have any tags")


print('\n')
print(f"-------- Untag AMI  ------------")
ami = session.client('ec2')
response = ami.describe_images(Owners=['174241535978'])
#paginator = ami.get_paginator('describe_images')
#for page in paginator.paginate(Owners=['117390685755']):
for i in response['Images']:
        amiid = i['ImageId']
        aminame = i['Name']
        try:
            tags = i['Tags']
        except KeyError:
            print(f"The AMI {aminame} does not have any tags")

