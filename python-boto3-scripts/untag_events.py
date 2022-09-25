import boto3
import csv
import json

session = boto3.Session(
        #profile_name='outlook'
        profile_name='moreretail-infra-cli'
        )

event = session.client('events')
events_rule = event.list_rules()
print("Event Rule Name")

for rule in events_rule['Rules']:
    rulename = rule['Name']
    rulearn = rule['Arn']
    #print("RuleName: {0}\nRuleARN: {1}\n".format(rulename,rulearn))
    tagresponse = event.list_tags_for_resource(ResourceARN=rulearn)
    if tagresponse['Tags'] == []:
    #if tagresponse['Tags'] == {}:
      print("The Event Rule",rulename,"does not have any Tags")

    #elif tagresponse['Tags'] != []:
    #elif tagresponse['Tags'] != {}:
    #  print("The Event Rule",rulename,"does have Tags",tagresponse['Tags'])


