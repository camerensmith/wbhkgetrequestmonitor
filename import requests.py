import requests
import json


webhook_url = 'http://128.0.0.1:5000/webhook'

data = {'name': 'Tracking Info', 'Target': 'https://www.soar.sh'}

r = requests.post(webhook_url, data=json.dumps(data), headers={'Content Type': 'application/json'})
print(webhook_url + r.json()['uuid'])

#Replace with info
#json = {
#    "default_status" : 200,
#    "default_content" : "Running",
#    "default_content_type" : "text/html",
#}

#replace with info
#headers = {
#    "api-key": "XXXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX" 
#}

#r = requests.post('https://webhook.site/token' json=json, headers=headers)
#print('Url Created: https://webhook.site/' +r.json()['uuid'])


#Replace with info
#token_id = "XXXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX" 
#headers = {"api-key": "XXXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX"}

#r = requests.get('https://webhook.site/token/' + token_id + '/requests?sorting=newest', headers=headers)

for request in r.json()['data']:
    print(request)
