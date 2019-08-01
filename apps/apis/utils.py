import requests
import json

ADAPTER_ID = 'barter-test'
BARTER_DASH_OID = 'barter-micropayment-dash'
BARTER_BITCOIN_OID = 'barter-micropayment-bitcoin'
BARTER_REPOSITORY_OID = 'barter-data-storage'

BITCOIN_CHANNEL = 'micropayments'
DASH_CHANNEL = 'micropayments'
REPOSITORY_CHANNEL = 'datasharing'

BARTER_URL = 'http://machine1.barter.block-chain-labs.com:4000'

DASH_PEERS = [
            "peer0.machine1.barter.block-chain-labs.com",
            "peer1.machine1.barter.block-chain-labs.com",
            "peer4.machine2.barter.block-chain-labs.com",
            "peer6.machine3.barter.block-chain-labs.com",
            "peer8.machine4.barter.block-chain-labs.com",
            "peer11.machine5.barter.block-chain-labs.com"
        ]

BITCOIN_PEERS = [
            "peer0.machine1.barter.block-chain-labs.com",
            "peer1.machine1.barter.block-chain-labs.com",
            "peer4.machine2.barter.block-chain-labs.com",
            "peer6.machine3.barter.block-chain-labs.com",
            "peer8.machine4.barter.block-chain-labs.com",
            "peer11.machine5.barter.block-chain-labs.com"
        ]

REPOSITORY_PEERS = [
            "peer0.machine1.barter.block-chain-labs.com",
            "peer2.machine1.barter.block-chain-labs.com",
            "peer5.machine2.barter.block-chain-labs.com",
            "peer7.machine3.barter.block-chain-labs.com",
            "peer9.machine4.barter.block-chain-labs.com",
            "peer12.machine5.barter.block-chain-labs.com"
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
