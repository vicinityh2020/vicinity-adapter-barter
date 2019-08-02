import json
import requests
import random
import string

from celery import shared_task
from celery.utils.log import get_task_logger
from .utils import *
from config.celery_app import app

logger = get_task_logger(__name__)


def random_string_digits(string_length=32):
    """Generate a random string of letters and digits """
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(string_length))


@shared_task
def instantiate_dash_wallet(token, network_type, wallet_secret, oid, aid):

    # Call API to install wallet chaincode
    url = '{url}/chaincodes'.format(url=BARTER_URL)
    wallet_name = random_string_digits()  # random wallet name
    payload = {
        "peers": DASH_PEERS,
        "chaincodeName": wallet_name,
        "chaincodePath": "/home/chainrider-56c03/contracts/dash/",
        "chaincodeType": "node",
        "chaincodeVersion": "v0"
    }
    headers = {'Content-Type': 'application/json',
               'Authorization': 'Bearer {}'.format(token)}
    try:
        r = requests.post(url, headers=headers, data=json.dumps(payload))
        res = r.json()
        if not res['success']:
            message = res['message']
            # send info about failed action and finish task
            data = {
                'error': message
            }
            url = 'http://localhost:9997/agent/actions/{}'.format(aid)
            headers = {'infrastructure-id': BARTER_DASH_OID, 'status': 'failed',
                       'adapter-id': ADAPTER_ID}
            r = requests.put(url, data=json.dumps(data), headers=headers)
            return
    except Exception as e:
        print(e)
        # send info about failed action and finish task
        data = {
            'error': 'Failed to install smart contract.'
        }
        url = 'http://localhost:9997/agent/actions/{}'.format(aid)
        headers = {'infrastructure-id': BARTER_DASH_OID, 'status': 'failed',
                   'adapter-id': ADAPTER_ID}
        r = requests.put(url, data=json.dumps(data), headers=headers)
        return

    # Call API to instantiate wallet chaincode
    url = '{url}/channels/{channel}/chaincodes'.format(url=BARTER_URL, channel=DASH_CHANNEL)
    payload = {
        "chaincodeName": wallet_name,
        "chaincodeVersion": "v0",
        "chaincodeType": "node",
        "args": [network_type, wallet_secret],
        "policy": {
            "identities": [
                {"role":
                    {
                        "name": "member",
                        "mspId": "barterMSP"
                    }
                }
            ],
            "policy": {
                "1-of":[ {"signed-by": 0} ]
            }
        }
    }
    headers = {'Content-Type': 'application/json',
               'Authorization': 'Bearer {}'.format(token)}
    try:
        r = requests.post(url, headers=headers, data=json.dumps(payload))
        res = r.json()
        if not res['success']:
            message = res['message']
            # send info about failed action and finish task
            data = {
                'error': message
            }
            url = 'http://localhost:9997/agent/actions/{}'.format(aid)
            headers = {'infrastructure-id': BARTER_DASH_OID, 'status': 'failed',
                       'adapter-id': ADAPTER_ID}
            r = requests.put(url, data=json.dumps(data), headers=headers)
            return
        # store wallet info in the db
        # TODO

        # send info about action completed
        data = {
            'wallet_name': wallet_name
        }
        url = 'http://localhost:9997/agent/actions/{}'.format(aid)
        headers = {'infrastructure-id': BARTER_DASH_OID, 'status': 'finished',
                   'adapter-id': ADAPTER_ID}
        r = requests.put(url, data=json.dumps(data), headers=headers)

    except Exception as e:
        print(e)
        # send info about failed action and finish task
        data = {
            'error': 'Failed to instantiate smart contract'
        }
        url = 'http://localhost:9997/agent/actions/{}'.format(aid)
        headers = {'infrastructure-id': BARTER_DASH_OID, 'status': 'failed',
                   'adapter-id': ADAPTER_ID}
        r = requests.put(url, data=json.dumps(data), headers=headers)


@shared_task
def instantiate_bitcoin_wallet(token, network_type, wallet_secret, oid, aid):
    # Call API to install wallet chaincode
    url = '{url}/chaincodes'.format(url=BARTER_URL)
    wallet_name = random_string_digits()  # random wallet name
    payload = {
        "peers": BITCOIN_PEERS,
        "chaincodeName": wallet_name,
        "chaincodePath": "/home/chainrider-56c03/contracts/bitcoin/",
        "chaincodeType": "node",
        "chaincodeVersion": "v0"
    }
    headers = {'Content-Type': 'application/json',
               'Authorization': 'Bearer {}'.format(token)}
    try:
        r = requests.post(url, headers=headers, data=json.dumps(payload))
        res = r.json()
        if not res['success']:
            message = res['message']
            # send info about failed action and finish task
            data = {
                'error': message
            }
            url = 'http://localhost:9997/agent/actions/{}'.format(aid)
            headers = {'infrastructure-id': BARTER_BITCOIN_OID, 'status': 'failed',
                       'adapter-id': ADAPTER_ID}
            r = requests.put(url, data=json.dumps(data), headers=headers)
            return
    except Exception as e:
        print(e)
        # send info about failed action and finish task
        data = {
            'error': 'Failed to install smart contract.'
        }
        url = 'http://localhost:9997/agent/actions/{}'.format(aid)
        headers = {'infrastructure-id': BARTER_BITCOIN_OID, 'status': 'failed',
                   'adapter-id': ADAPTER_ID}
        r = requests.put(url, data=json.dumps(data), headers=headers)
        return

    # Call API to instantiate wallet chaincode
    url = '{url}/channels/{channel}/chaincodes'.format(url=BARTER_URL, channel=BITCOIN_CHANNEL)
    payload = {
        "chaincodeName": wallet_name,
        "chaincodeVersion": "v0",
        "chaincodeType": "node",
        "args": [network_type, wallet_secret],
        "policy": {
            "identities": [
                {"role":
                    {
                        "name": "member",
                        "mspId": "barterMSP"
                    }
                }
            ],
           "policy": {
                "1-of":[ {"signed-by": 0} ]
            }
        }
    }
    headers = {'Content-Type': 'application/json',
               'Authorization': 'Bearer {}'.format(token)}
    try:
        r = requests.post(url, headers=headers, data=json.dumps(payload))
        res = r.json()
        if not res['success']:
            # send info about failed action and finish task
            message = res['message']
            data = {
                'error': message
            }
            url = 'http://localhost:9997/agent/actions/{}'.format(aid)
            headers = {'infrastructure-id': BARTER_BITCOIN_OID, 'status': 'failed',
                       'adapter-id': ADAPTER_ID}
            r = requests.put(url, data=json.dumps(data), headers=headers)
            return

        # store wallet info in the db

        # send info about action completed
        data = {
            'wallet_name': wallet_name
        }
        url = 'http://localhost:9997/agent/actions/{}'.format(aid)
        headers = {'infrastructure-id': BARTER_BITCOIN_OID, 'status': 'finished',
                   'adapter-id': ADAPTER_ID}
        r = requests.put(url, data=json.dumps(data), headers=headers)
    except Exception as e:
        print(e)
        # send info about failed action and finish task
        data = {
            'error': 'Failed to instantiate smart contract'
        }
        url = 'http://localhost:9997/agent/actions/{}'.format(aid)
        headers = {'infrastructure-id': BARTER_BITCOIN_OID, 'status': 'failed',
                   'adapter-id': ADAPTER_ID}
        r = requests.put(url, data=json.dumps(data), headers=headers)

@shared_task
def instantiate_data_storage(token, secret, oid, aid):
    # Call API to install wallet chaincode
    url = '{url}/chaincodes'.format(url=BARTER_URL)
    repo_name = random_string_digits()  # random wallet name
    payload = {
        "peers": REPOSITORY_PEERS,
        "chaincodeName": repo_name,
        "chaincodePath": "/home/chainrider-56c03/contracts/data_storage/",
        "chaincodeType": "node",
        "chaincodeVersion": "v0"
    }
    headers = {'Content-Type': 'application/json',
               'Authorization': 'Bearer {}'.format(token)}
    try:
        r = requests.post(url, headers=headers, data=json.dumps(payload))
        res = r.json()
        if not res['success']:
            message = res['message']
            # send info about failed action and finish task
            data = {
                'error': message
            }
            url = 'http://localhost:9997/agent/actions/{}'.format(aid)
            headers = {'infrastructure-id': BARTER_REPOSITORY_OID, 'status': 'failed',
                       'adapter-id': ADAPTER_ID}
            r = requests.put(url, data=json.dumps(data), headers=headers)
            return
    except Exception as e:
        print(e)
        # send info about failed action and finish task
        data = {
            'error': 'Failed to install smart contract.'
        }
        url = 'http://localhost:9997/agent/actions/{}'.format(aid)
        headers = {'infrastructure-id': BARTER_REPOSITORY_OID, 'status': 'failed',
                   'adapter-id': ADAPTER_ID}
        r = requests.put(url, data=json.dumps(data), headers=headers)
        return

    # Call API to instantiate wallet chaincode
    url = '{url}/channels/{channel}/chaincodes'.format(url=BARTER_URL, channel=REPOSITORY_CHANNEL)
    payload = {
        "chaincodeName": repo_name,
        "chaincodeVersion": "v0",
        "chaincodeType": "node",
        "args": [secret],
        "policy": {
            "identities": [
                {"role":
                    {
                        "name": "member",
                        "mspId": "barterMSP"
                    }
                }
            ],
           "policy": {
                "1-of":[ {"signed-by": 0} ]
            }
        }
    }
    headers = {'Content-Type': 'application/json',
               'Authorization': 'Bearer {}'.format(token)}
    try:
        r = requests.post(url, headers=headers, data=json.dumps(payload))
        res = r.json()
        if not res['success']:
            # send info about failed action and finish task
            message = res['message']
            data = {
                'error': message
            }
            url = 'http://localhost:9997/agent/actions/{}'.format(aid)
            headers = {'infrastructure-id': BARTER_REPOSITORY_OID, 'status': 'failed',
                       'adapter-id': ADAPTER_ID}
            r = requests.put(url, data=json.dumps(data), headers=headers)
            return

        # store wallet info in the db

        # send info about action completed
        data = {
            'repository_name': repo_name
        }
        url = 'http://localhost:9997/agent/actions/{}'.format(aid)
        headers = {'infrastructure-id': BARTER_REPOSITORY_OID, 'status': 'finished',
                   'adapter-id': ADAPTER_ID}
        r = requests.put(url, data=json.dumps(data), headers=headers)
    except Exception as e:
        print(e)
        # send info about failed action and finish task
        data = {
            'error': 'Failed to instantiate smart contract'
        }
        url = 'http://localhost:9997/agent/actions/{}'.format(aid)
        headers = {'infrastructure-id': BARTER_REPOSITORY_OID, 'status': 'failed',
                   'adapter-id': ADAPTER_ID}
        r = requests.put(url, data=json.dumps(data), headers=headers)