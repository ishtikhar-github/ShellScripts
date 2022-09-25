import boto3
import csv
import json

session = boto3.Session(
        #profile_name='outlook',
        profile_name='moreretail-infra-cli'
        #region_name='ap-south-1'
        )
elbv1 = session.client('elb')
response = elbv1.describe_load_balancers()
print('\n')
print(f"-------- Untag Classic ELBS ------------")
for i in response['LoadBalancerDescriptions']:
     elb_name = i['LoadBalancerName']
     #print(elb_name)
     tagresponse = elbv1.describe_tags(LoadBalancerNames=[elb_name])
     for tags in tagresponse['TagDescriptions']: 
      tag = tags['Tags']
      if tag == []:
        print(f"The ELB {elb_name} does not have any tags")

      #elif tag != []:
      #  print(f"The ELB {elb_name} does have tags {tag}")





elbv2 = session.client('elbv2')
response = elbv2.describe_load_balancers()
print('\n')
print(f"-------- Untag Application and Network LB ------------")

for i in response['LoadBalancers']:
     elb_name = i['LoadBalancerName']
     elb_arn = i['LoadBalancerArn']
     #print(elb_name)
     tagresponse = elbv2.describe_tags(ResourceArns=[elb_arn])
     for tags in tagresponse['TagDescriptions']: 
        tag = tags['Tags']
        if tag == []:
            print(f"The ELB {elb_name} does not have any tags")

        #elif tag != []:
        #    print(f"The ELB {elb_name} does have tags {tag}")

tg = elbv2.describe_target_groups()
print('\n')
print(f"-------- Untag ELB Target Group ------------")

for i in tg['TargetGroups']:
     tg_name = i['TargetGroupName']
     tg_arn = i['TargetGroupArn']
     tagresponse = elbv2.describe_tags(ResourceArns=[tg_arn])
     for tags in tagresponse['TagDescriptions']:
        tag = tags['Tags']
        if tag == []:
            print(f"The ELB Target Group {tg_name} does not have any tags")

        #elif tag != []:
        #    print(f"The ELB {tg_name} does have tags {tag}")

print('\n')
print(f"-------- Untag Auto Scaling Group ------------")
asg = session.client('autoscaling')
asgresponse = asg.describe_auto_scaling_groups()
for i in asgresponse['AutoScalingGroups']:
    asg_name = i['AutoScalingGroupName']
    asg_arn = i['AutoScalingGroupARN']
    tags = i['Tags']
    if tags == []:
        print(f" The Auto Scaling Group {asg_name} does not have any tags")
    #elif tags != []:
    #    print(f" The Auto Scaling Group {asg_name} does have tags {tags}")


