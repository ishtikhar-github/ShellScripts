#https://www.ipswitch.com/blog/how-to-manage-aws-iam-users-with-python
import boto3
import csv
import json

session = boto3.Session(
        #profile_name='outlook'
        profile_name='default'
        )

iam = session.client('iam')
#iamusers = iam.list_users()
#users = iamusers['Users']
paginator = iam.get_paginator('list_users')
print("IAM UserName")
l = []


#for x in iamusers['Users']:
for page in paginator.paginate():
 #for user in users:
 for user in page['Users']:
  #print (user['UserName']) 
   user_name = user['UserName']
   List_of_Inline_Policies =  iam.list_user_policies(UserName=user_name)
   user_groups = iam.list_groups_for_user(UserName=user_name)
   List_of_managed_user_policies = iam.list_attached_user_policies(UserName=user_name)
   d = {}
   d['UserName'] = user_name
   d['GroupName'] = []
   d['ManagedPolicy'] = []
   d['InlinePolicy'] = []


   # Get list of user Groups
   for group in user_groups['Groups']:
       group_name = group['GroupName']
       print("Iam user", user_name, " is a member of group",group_name)
       d['GroupName'].append(group_name)


   # Get list of Managed policy
   for key in List_of_managed_user_policies['AttachedPolicies']:
       managed_policy = key['PolicyName']
       print("IAM User",user_name,"having managed policy",key['PolicyName'])
       d['ManagedPolicy'].append(managed_policy)


   # Get list of Inline policy
   for key in List_of_Inline_Policies['PolicyNames']:
       print("IAM User",user_name,"having inline policy",key)
       d['InlinePolicy'].append(key)
   l.append(d)
 
# CSV headers
csv_headers = ['UserName', 'GroupName', 'ManagedPolicy','InlinePolicy']
filename = "iamusers.csv"
# Open csv file in write mode
for dd in l:
    #dd['UserName'] = ",".join(dd['UserName'])
    dd['GroupName'] = ",".join(dd['GroupName'])
    dd['ManagedPolicy'] = ",".join(dd['ManagedPolicy'])
    dd['InlinePolicy'] = ",".join(dd['InlinePolicy'])
with open(filename, 'a', newline='') as csvFile:
     writer = csv.DictWriter(csvFile,fieldnames = csv_headers)
   # Write headers
   #  writer.writeheader()
   # writing data rows
     writer.writerows(l)






#      data_to_be_inserted_in_csv.append({
#                "UserName": user_name,
#                "GroupName": group_name,
#                "Managed Policy": managed_policy,
#                "Inline POlicy": key
#            })
#
#if data_to_be_inserted_in_csv:
#        keys = list(data_to_be_inserted_in_csv[0].keys())
#        #print(keys)
#        with open('iamusers.csv', 'a', newline='') as output_file:
#            dict_writer = csv.DictWriter(output_file, fieldnames=keys)
#            #dict_writer.writeheader()
#            dict_writer.writerows(data_to_be_inserted_in_csv)
    


   

#response = iam.list_groups()
#for group in response['Groups']:    
#    group_details = iam.get_group(GroupName=group['GroupName'])
#    print(group['GroupName'])
#    for user in group_details['Users']:
#        print(" - ", user['UserName'])

