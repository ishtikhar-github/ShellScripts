import json
import os
import webbrowser
from time import time, sleep
from boto3.session import Session

session = Session()
account_id = '870421249093'
start_url = 'https://moreretail.awsapps.com/start'
region = 'ap-south-1' 
sso_oidc = session.client('sso-oidc')
client_creds = sso_oidc.register_client(
    clientName='mohdishtikhar.khan',
    clientType='public',
)
device_authorization = sso_oidc.start_device_authorization(
    clientId=client_creds['clientId'],
    clientSecret=client_creds['clientSecret'],
    startUrl=start_url,
)
print(f"TemporaryCreds:{client_creds}")
print(f"DeviceAuthorization:{device_authorization}")
url = device_authorization['verificationUriComplete']   
device_code = device_authorization['deviceCode']
expires_in = device_authorization['expiresIn']
interval = device_authorization['interval']
print(url)
print(device_code)
print(expires_in)
print(interval)
#webbrowser.open(url,new=2, autoraise=True)
chrome_path = '/usr/bin/google-chrome %s'
webbrowser.get(chrome_path).open(url)
#for n in range(1, expires_in // interval + 1):
#    sleep(interval)
#    try:
#        token = sso_oidc.create_token(
#            grantType='urn:ietf:params:oauth:grant-type:device_code',
#            deviceCode=device_code,
#            clientId=client_creds['clientId'],
#            clientSecret=client_creds['clientSecret'],
#        )
#        print("creation_of_token")
#        break
#    except sso_oidc.exceptions.AuthorizationPendingException:
#        pass
# 
