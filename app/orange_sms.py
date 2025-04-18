import requests
from flask import current_app

def get_access_token():
    url = 'https://api.orange.com/oauth/v3/token'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = {'grant_type': 'client_credentials'}
    auth = (current_app.config['CLIENT_ID'], current_app.config['CLIENT_SECRET'])

    response = requests.post(url, headers=headers, data=data, auth=auth)
    response.raise_for_status()
    return response.json()['access_token']

def send_sms(to, message):
    token = get_access_token()
    #sender = current_app.config['SENDER_ADDRESS']
    sender = current_app.config['SENDER_ADDRESS'].replace("tel:", "")

    url = f'https://api.orange.com/smsmessaging/v1/outbound/{sender}/requests'
     #url = "https://api.orange.com/smsmessaging/v1/outbound/tel%3A+221779607461/requests"

    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }

    payload = {
        'outboundSMSMessageRequest': {
            'address': to,
            'senderAddress': sender,
            'outboundSMSTextMessage': {
                'message': message
            }
        }
    }

    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()