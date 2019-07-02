import requests
import json

ADAPTER_ID = 'barter-test'
BARTER_DASH_OID = 'barter-micropayment-dash'
BARTER_BITCOIN_OID = 'barter-micropayment-bitcoin'
BARTER_REPOSITORY_OID = 'barter-data-storage'

BITCOIN_CHANNEL = 'test'
DASH_CHANNEL = 'test'
REPOSITORY_CHANNEL = 'test'

BARTER_URL = 'http://machine1.barter.block-chain-labs.com:4000'

BARTER_PEER = 'peer3.machine2.barter.block-chain-labs.com'

DASH_PEERS = [
            "peer0.machine1.barter.block-chain-labs.com",
            "peer3.machine2.barter.block-chain-labs.com",
            "peer10.machine5.barter.block-chain-labs.com"
        ]

BITCOIN_PEERS = [
            "peer0.machine1.barter.block-chain-labs.com",
            "peer3.machine2.barter.block-chain-labs.com",
            "peer10.machine5.barter.block-chain-labs.com"
        ]

REPOSITORY_PEERS = [
            "peer0.machine1.barter.block-chain-labs.com",
            "peer3.machine2.barter.block-chain-labs.com",
            "peer10.machine5.barter.block-chain-labs.com"
        ]

def get_access_token():
    url = '{url}/users/register'.format(url=BARTER_URL)
    payload = {
        "username": "barter",
        "orgName": "barter",
        "role": "client",
        "secret": "cb164edfcd6a528704b674684a5d0261"
    }
    headers = {'Content-Type': 'application/json'}
    try:
        r = requests.post(url, headers=headers, data=json.dumps(payload))
        data = r.json()
        if data and data['success']:
            return data['token']
        return False
    except Exception as e:
        print(e)
        return False
