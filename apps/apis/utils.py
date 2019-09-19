import requests
import json
import itertools

ADAPTER_ID = 'barter-test'
BARTER_DASH_OID = 'barter-micropayment-dash'
BARTER_BITCOIN_OID = 'barter-micropayment-bitcoin'
BARTER_REPOSITORY_OID = 'barter-data-storage'

BITCOIN_CHANNEL = 'micropayments'
DASH_CHANNEL = 'micropayments'
REPOSITORY_CHANNEL = 'datasharing'

BARTER_REST_API_LIST = ['http://machine1.barter.block-chain-labs.com:4000',
                        'http://machine2.barter.block-chain-labs.com:4000',
                        'http://machine3.barter.block-chain-labs.com:4000',
                        'http://machine4.barter.block-chain-labs.com:4000',
                        'http://machine5.barter.block-chain-labs.com:4000'
                        ]

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

url_round_r = itertools.cycle(BARTER_REST_API_LIST)
micropayment_dash_peers_rr = itertools.cycle(DASH_PEERS)
micropayment_bitcoin_peers_rr = itertools.cycle(BITCOIN_PEERS)
repository_peers_rr = itertools.cycle(REPOSITORY_PEERS)


def get_access_token(rest_url):
    url = '{url}/users/register'.format(url=rest_url)
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


def get_rest_url():
    return next(url_round_r)


def get_dash_peer():
    return next(micropayment_dash_peers_rr)


def get_bitcoin_peer():
    return next(micropayment_bitcoin_peers_rr)


def get_repository_peer():
    return next(repository_peers_rr)
