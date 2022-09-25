import boto3
import csv
import json

session = boto3.Session(
        #profile_name='outlook'
        profile_name='moreretail-infra-cli'
        )

vpc = session.client('ec2')
response = vpc.describe_vpcs()
#print(response)
print(f"-------- Untag VPC ----------------")
for i in response['Vpcs']:
    vpcid = i['VpcId']
    try:
        tags = i['Tags']
    except KeyError:
        print(f"No tags found for vpc {vpcid}")


print('\n')
print(f"-------- Untag Subnets ------------")
subnet_response = vpc.describe_subnets()
#print(response)
for i in subnet_response['Subnets']:
        subnetid = i['SubnetId']
        try:
           tags = i['Tags']
        except KeyError:
           print(f"No tags found for subnet {subnetid}")


print('\n')
print(f"-------- Untag Route Tables ------------")
rt = vpc.describe_route_tables()
#print(rt)
for i in rt['RouteTables']:
     rtid = i['RouteTableId']
     #print(rtid)
     #print(i['Tags'])
     tags = i['Tags']
     if tags == []:
         print(f"No tags found for route table {rtid}")
     #elif tags != []:
     #    print(f"the route table {rtid} does have tags {tags}")


print('\n')
print(f"-------- Untag Internet Gateways ------------")
igw = vpc.describe_internet_gateways()
for i in igw['InternetGateways']:
      igwid = i['InternetGatewayId']
      tags = i['Tags']
      if tags == []:
         print(f"No tags found for internet gateway {igwid} ")



print('\n')
print(f"-------- Untag EIPs ------------")
eip = vpc.describe_addresses()
for i in eip['Addresses']:
    eid = i['AllocationId']
    try:
      tags = i['Tags']
    except KeyError:
      print(f"No tags found for eip {eid}")

print('\n')
print(f"-------- Untag Nat Gateways ------------")
ngw = vpc.describe_nat_gateways()
for i in ngw['NatGateways']:
      ngwid = i['NatGatewayId']
      tags = i['Tags']
      #print(tags)


print('\n')
print(f"-------- Untag NACL ------------")
nacl = vpc.describe_network_acls()
for i in nacl['NetworkAcls']:
    naclid = i['NetworkAclId']
    tags = i['Tags']
    if tags == []:
         print(f"No tags found for network acl {naclid} ")

print('\n')
print(f"-------- Untag Security Groups ------------")
#sg = vpc.describe_security_groups()
paginator = vpc.get_paginator('describe_security_groups')
for page in paginator.paginate():
 for i in page['SecurityGroups']:
   sgname = i['GroupName']
   try:
      tags = i['Tags']
   except KeyError:
      print(f"No tags found for {sgname}")

   
