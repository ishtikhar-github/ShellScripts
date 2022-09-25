import boto3

#session = boto3.Session()
session = boto3.Session(
        region_name='ap-south-1',
        profile_name='moreretail-infra-cli'
        )

ec2 = session.client('ec2')

response = ec2.describe_instances()

obj_number = len(response['Reservations'])

for objects in range(obj_number):
    try:
        z = response['Reservations'][objects]['Instances'][0]['Tags'][0]['Key']
    except KeyError as e:
        untagged_instanceid = response['Reservations'][objects]['Instances'][0]['InstanceId']
        untagged_state = response['Reservations'][objects]['Instances'][0]['State']['Name']
        #untagged_keyname = response['Reservations'][objects]['Instances'][0]['KeyName']
        print("InstanceID: {0}, RunningState: {1}".format(untagged_instanceid, untagged_state))


#import boto3
#session = boto3.Session(
#        region_name='eu-west-1',
#        profile_name='myprofile'
#        )

#ec2 = session.client('ec2')

#response = ec2.describe_instances()

#obj_number = len(response['Reservations'])

#for objects in xrange(obj_number):
#    try:
#        z = response['Reservations'][objects]['Instances'][0]['Tags'][0]['Key']
#    except KeyError as e:
#        untagged_instanceid = response['Reservations'][objects]['Instances'][0]['InstanceId']
#        untagged_state = response['Reservations'][objects]['Instances'][0]['State']['Name']
#        print("InstanceID: {0}, RunningState: {1}".format(untagged_instanceid, untagged_state))

