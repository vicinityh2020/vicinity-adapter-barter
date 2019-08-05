import json
from datetime import datetime, timezone, timedelta
import random
import requests
import rest_framework.status as status
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView

import logging
logger = logging.getLogger(__name__)

from .tasks import instantiate_dash_wallet, instantiate_bitcoin_wallet, instantiate_data_storage
from .thing_descriptors import *
from .utils import *


class ObjectsView(APIView):
    service_object_descriptor = {
        'adapter-id': ADAPTER_ID,
        'thing-descriptions': [
            {
                'oid': BARTER_DASH_OID,
                'name': 'VLF Barter MicroPayment Service based on DASH cryptocurrency',
                'type': 'core:Service',
                'version': '0.1',
                'keywords': ['micropayment', 'dash', 'wallet'],
                'properties': [MY_BALANCE_DASH, MY_FUNDING_ADDRESS_DASH, PAYMENT_ADDRESS_DASH, TICKER_DASH,
                               PRIVATE_KEY_DASH, SEND_PAYMENT_DASH],
                'events': [PAYMENT_EVENT_DASH],
                'actions': [ACTION_WALLET_SETUP_DASH, ACTION_WALLET_RECOVER_DASH]
            },
            {
                'oid': BARTER_BITCOIN_OID,
                'name': 'VLF Barter MicroPayment Service based on BITCOIN cryptocurrency',
                'type': 'core:Service',
                'version': '0.1',
                'keywords': ['micropayment', 'bitcoin', 'wallet'],
                'properties': [MY_BALANCE_BITCOIN, MY_FUNDING_ADDRESS_BITCOIN, PAYMENT_ADDRESS_BITCOIN, TICKER_BITCOIN,
                               PRIVATE_KEY_BITCOIN, SEND_PAYMENT_BITCOIN],
                'events': [PAYMENT_EVENT_BITCOIN],
                'actions': [ACTION_WALLET_SETUP_BITCOIN, ACTION_WALLET_RECOVER_BITCOIN]
            },
            {
                'oid': BARTER_REPOSITORY_OID,
                'name': 'VLF Barter Service for data management on permissioned blockchain',
                'type': 'core:Service',
                'version': '0.1',
                'keywords': ['data', 'repository'],
                'properties': [CREATE_ASSET, READ_ASSET_BY_KEY, UPDATE_ASSET, INVALIDATE_ASSET,
                               READ_ASSETS_BY_KEY_RANGE, READ_ASSET_HISTORY, COUCHDB_QUERY_ASSETS],
                'actions': [SETUP_REPOSITORY],
                'events': []
            }
        ]
    }

    def get(self, request):
        return Response(self.service_object_descriptor, status=status.HTTP_200_OK)


class WalletActionsDash(APIView):

    def delete(self, request, oid, aid):
        return Response({}, status=status.HTTP_200_OK)

    def post(self, request, oid, aid):
        input_data = request.data
        if aid not in AID_DASH:
            data = {
                'error': True,
                'message': 'Invalid AID',
                'status': status.HTTP_404_NOT_FOUND
            }
            return Response(data, status=status.HTTP_404_NOT_FOUND)

        if not input_data:
            data = {
                'error': 'Missing input parameters'
            }
            url = 'http://localhost:9997/agent/actions/{}'.format(aid)
            headers = {'infrastructure-id': BARTER_DASH_OID, 'status': 'failed',
                       'adapter-id': ADAPTER_ID}
            r = requests.put(url, data=json.dumps(data), headers=headers)
            data = {
                'error': True,
                'message': 'Missing input parameters',
                'status': status.HTTP_400_BAD_REQUEST
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

        # Get authentication token
        token = get_access_token()
        if not token:
            data = {
                'error': 'Blockchain authentication failed'
            }
            url = 'http://localhost:9997/agent/actions/{}'.format(aid)
            headers = {'infrastructure-id': BARTER_DASH_OID, 'status': 'failed',
                       'adapter-id': ADAPTER_ID}
            r = requests.put(url, data=json.dumps(data), headers=headers)
            data = {
                'error': True,
                'message': 'Blockchain authentication failed',
                'status': status.HTTP_400_BAD_REQUEST
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

        if aid == 'wallet_setup':
            try:
                network_type = input_data['network_type']
                wallet_secret = input_data['wallet_secret']
                chainrider_token = input_data['chainrider_token']
            except Exception as e:
                logger.error(e)
                data = {
                    'error': 'Invalid input parameters'
                }
                url = 'http://localhost:9997/agent/actions/{}'.format(aid)
                headers = {'infrastructure-id': BARTER_DASH_OID, 'status': 'failed',
                           'adapter-id': ADAPTER_ID}
                r = requests.put(url, data=json.dumps(data), headers=headers)
                data = {
                    'error': True,
                    'message': 'Invalid input parameters',
                    'status': status.HTTP_400_BAD_REQUEST
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
            if network_type not in ['mainnet', 'testnet']:
                data = {
                    'error': 'Network type must be mainnet or testnet'
                }
                url = 'http://localhost:9997/agent/actions/{}'.format(aid)
                headers = {'infrastructure-id': BARTER_DASH_OID, 'status': 'failed',
                           'adapter-id': ADAPTER_ID}
                r = requests.put(url, data=json.dumps(data), headers=headers)
                data = {
                    'error': True,
                    'message': 'Network type must be mainnet or testnet',
                    'status': status.HTTP_400_BAD_REQUEST
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)

            # call celery task for wallet setup
            a = instantiate_dash_wallet.delay(token, network_type, wallet_secret, chainrider_token, private_key, oid, aid)
        elif aid == 'wallet_recover':
            try:
                network_type = input_data['network_type']
                wallet_secret = input_data['wallet_secret']
                chainrider_token = input_data['chainrider_token']
                private_key = input_data['private_key']
            except Exception as e:
                logger.error(e)
                data = {
                    'error': 'Invalid input parameters'
                }
                url = 'http://localhost:9997/agent/actions/{}'.format(aid)
                headers = {'infrastructure-id': BARTER_DASH_OID, 'status': 'failed',
                           'adapter-id': ADAPTER_ID}
                r = requests.put(url, data=json.dumps(data), headers=headers)
                data = {
                    'error': True,
                    'message': 'Invalid input parameters',
                    'status': status.HTTP_400_BAD_REQUEST
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
            if network_type not in ['mainnet', 'testnet']:
                data = {
                    'error': 'Network type must be mainnet or testnet'
                }
                url = 'http://localhost:9997/agent/actions/{}'.format(aid)
                headers = {'infrastructure-id': BARTER_DASH_OID, 'status': 'failed',
                           'adapter-id': ADAPTER_ID}
                r = requests.put(url, data=json.dumps(data), headers=headers)
                data = {
                    'error': True,
                    'message': 'Network type must be mainnet or testnet',
                    'status': status.HTTP_400_BAD_REQUEST
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)

            # call celery task for wallet setup
            a = instantiate_dash_wallet.delay(token, network_type, wallet_secret, chainrider_token, private_key, oid, aid)
        data = {}
        return Response(data, status=status.HTTP_200_OK)


class WalletActionsBitcoin(APIView):

    def delete(self, request, oid, aid):
        return Response({}, status=status.HTTP_200_OK)

    def post(self, request, oid, aid):
        input_data = request.data
        if aid not in AID_BITCOIN:
            data = {
                'error': True,
                'message': 'Invalid AID',
                'status': status.HTTP_404_NOT_FOUND
            }
            return Response(data, status=status.HTTP_404_NOT_FOUND)

        if not input_data:
            data = {
                'error': 'Missing input parameters'
            }
            url = 'http://localhost:9997/agent/actions/{}'.format(aid)
            headers = {'infrastructure-id': BARTER_DASH_OID, 'status': 'failed',
                       'adapter-id': ADAPTER_ID}
            r = requests.put(url, data=json.dumps(data), headers=headers)
            data = {
                'error': True,
                'message': 'Missing input parameters',
                'status': status.HTTP_400_BAD_REQUEST
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

        # Get authentication token
        token = get_access_token()
        if not token:
            data = {
                'error': 'Blockchain authentication failed'
            }
            url = 'http://localhost:9997/agent/actions/{}'.format(aid)
            headers = {'infrastructure-id': BARTER_DASH_OID, 'status': 'failed',
                       'adapter-id': ADAPTER_ID}
            r = requests.put(url, data=json.dumps(data), headers=headers)
            data = {
                'error': True,
                'message': 'Blockchain authentication failed',
                'status': status.HTTP_400_BAD_REQUEST
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

        if aid == 'wallet_setup':
            try:
                network_type = input_data['network_type']
                wallet_secret = input_data['wallet_secret']
                chainrider_token = input_data['chainrider_token']
            except Exception as e:
                logger.error(e)
                data = {
                    'error': 'Invalid input parameters'
                }
                url = 'http://localhost:9997/agent/actions/{}'.format(aid)
                headers = {'infrastructure-id': BARTER_DASH_OID, 'status': 'failed',
                           'adapter-id': ADAPTER_ID}
                r = requests.put(url, data=json.dumps(data), headers=headers)
                data = {
                    'error': True,
                    'message': 'Invalid input parameters',
                    'status': status.HTTP_400_BAD_REQUEST
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
            if network_type not in ['mainnet', 'testnet']:
                data = {
                    'error': 'Network type must be mainnet or testnet'
                }
                url = 'http://localhost:9997/agent/actions/{}'.format(aid)
                headers = {'infrastructure-id': BARTER_DASH_OID, 'status': 'failed',
                           'adapter-id': ADAPTER_ID}
                r = requests.put(url, data=json.dumps(data), headers=headers)
                data = {
                    'error': True,
                    'message': 'Network type must be mainnet or testnet',
                    'status': status.HTTP_400_BAD_REQUEST
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)

            # call celery task for wallet setup
            a = instantiate_bitcoin_wallet.delay(token, network_type, wallet_secret, chainrider_token, private_key, oid, aid)
        elif aid == 'wallet_recover':
            try:
                network_type = input_data['network_type']
                wallet_secret = input_data['wallet_secret']
                chainrider_token = input_data['chainrider_token']
                private_key = input_data['private_key']
            except Exception as e:
                logger.error(e)
                data = {
                    'error': 'Invalid input parameters'
                }
                url = 'http://localhost:9997/agent/actions/{}'.format(aid)
                headers = {'infrastructure-id': BARTER_DASH_OID, 'status': 'failed',
                           'adapter-id': ADAPTER_ID}
                r = requests.put(url, data=json.dumps(data), headers=headers)
                data = {
                    'error': True,
                    'message': 'Invalid input parameters',
                    'status': status.HTTP_400_BAD_REQUEST
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
            if network_type not in ['mainnet', 'testnet']:
                data = {
                    'error': 'Network type must be mainnet or testnet'
                }
                url = 'http://localhost:9997/agent/actions/{}'.format(aid)
                headers = {'infrastructure-id': BARTER_DASH_OID, 'status': 'failed',
                           'adapter-id': ADAPTER_ID}
                r = requests.put(url, data=json.dumps(data), headers=headers)
                data = {
                    'error': True,
                    'message': 'Network type must be mainnet or testnet',
                    'status': status.HTTP_400_BAD_REQUEST
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)

            # call celery task for wallet setup
            a = instantiate_bitcoin_wallet.delay(token, network_type, wallet_secret, chainrider_token, private_key, oid, aid)
        data = {}
        return Response(data, status=status.HTTP_200_OK)


class RepositoryActions(APIView):

    def delete(self, request, oid, aid):
        return Response({}, status=status.HTTP_200_OK)

    def post(self, request, oid, aid):
        input_data = request.data
        if aid not in AID_REPOSITORY:
            data = {
                'error': True,
                'message': 'Invalid AID',
                'status': status.HTTP_404_NOT_FOUND
            }
            return Response(data, status=status.HTTP_404_NOT_FOUND)

        if not input_data:
            data = {
                'error': True,
                'message': 'Missing input parameters',
                'status': status.HTTP_400_BAD_REQUEST
            }
            url = 'http://localhost:9997/agent/actions/{}'.format(aid)
            headers = {'infrastructure-id': BARTER_REPOSITORY_OID, 'status': 'failed',
                       'adapter-id': ADAPTER_ID}
            r = requests.put(url, data=json.dumps(data), headers=headers)
            data = {
                'error': True,
                'message': 'Missing input parameters',
                'status': status.HTTP_400_BAD_REQUEST
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

        # Get authentication token
        token = get_access_token()
        if not token:
            data = {
                'error': True,
                'message': 'Blockchain authentication failed',
                'status': status.HTTP_400_BAD_REQUEST
            }
            url = 'http://localhost:9997/agent/actions/{}'.format(aid)
            headers = {'infrastructure-id': BARTER_REPOSITORY_OID, 'status': 'failed',
                       'adapter-id': ADAPTER_ID}
            r = requests.put(url, data=json.dumps(data), headers=headers)
            data = {
                'error': True,
                'message': 'Blockchain authentication failed',
                'status': status.HTTP_400_BAD_REQUEST
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        if aid == 'repository_setup':
            try:
                repository_secret = input_data['repository_secret']
            except Exception as e:
                data = {
                    'error': True,
                    'message': 'Invalid input parameters',
                    'status': status.HTTP_400_BAD_REQUEST
                }
                url = 'http://localhost:9997/agent/actions/{}'.format(aid)
                headers = {'infrastructure-id': BARTER_REPOSITORY_OID, 'status': 'failed',
                           'adapter-id': ADAPTER_ID}
                r = requests.put(url, data=json.dumps(data), headers=headers)
                data = {
                    'error': True,
                    'message': 'Invalid input parameters',
                    'status': status.HTTP_400_BAD_REQUEST
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
            a = instantiate_data_storage.delay(token, repository_secret, oid, aid)
        data = {}
        return Response(data, status=status.HTTP_200_OK)


class WalletViewDash(APIView):

    def put(self, request, pid):
        input_data = request.data
        if pid not in PID_DASH:
            data = {
                'error': True,
                'message': 'Invalid PID',
                'status': status.HTTP_404_NOT_FOUND
            }
            return Response(data, status=status.HTTP_404_NOT_FOUND)

        if not input_data:
            data = {
                'error': True,
                'message': 'Missing input parameters',
                'status': status.HTTP_400_BAD_REQUEST
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

        # Get authentication token
        token = get_access_token()
        if not token:
            data = {
                'error': True,
                'message': 'Blockchain authentication failed',
                'status': status.HTTP_400_BAD_REQUEST
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        res = dict()

        if pid == 'my_balance':
            try:
                wallet_name = input_data['wallet_name']
                wallet_secret = input_data['wallet_secret']
            except Exception as e:
                logger.error(e)
                data = {
                    'error': True,
                    'message': 'Invalid input parameters',
                    'status': status.HTTP_400_BAD_REQUEST
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)

            # call API for wallet balance
            url = '{url}/channels/{channel}/chaincodes/{chaincode}'.format(url=BARTER_URL, channel=DASH_CHANNEL,
                                                                           chaincode=wallet_name)
            peer = random.choice(DASH_PEERS)
            logger.error('Running action on peer: {}'.format(peer))
            payload = {'peer': peer, 'fcn': 'getBalance', 'args': '["{}"]'.format(wallet_secret)}
            headers = {'Content-Type': 'application/json',
                       'Authorization': 'Bearer {}'.format(token)}
            try:
                r = requests.get(url, headers=headers, params=payload)
                res = r.json()
                data = {
                    'wallet_address': res['addrStr'],
                    'balance_dash': res['balance'],
                    'balance_duffs': res['balanceSat'],
                    'total_received_dash': res['totalReceived'],
                    'total_received_duffs': res['totalReceivedSat'],
                    'total_sent_dash': res['totalSent'],
                    'total_sent_duffs': res['totalSentSat'],
                    'unconfirmed_balance_dash': res['unconfirmedBalance'],
                    'unconfirmed_balance_duffs': res['unconfirmedBalanceSat'],
                    'unconfirmed_appearances': res['unconfirmedAppearances'],
                    'tx_appearances': res['txAppearances']
                }
            except Exception as e:
                logger.error(e)
                message = "Unknown error"
                if res:
                    message = res['message'] if 'message' in res else 'Unknown error'
                data = {
                    'error': True,
                    'message': message,
                    'status': status.HTTP_400_BAD_REQUEST
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)

        elif pid == 'my_funding_address':
            try:
                wallet_name = input_data['wallet_name']
                wallet_secret = input_data['wallet_secret']
            except Exception as e:
                logger.error(e)
                data = {
                    'error': True,
                    'message': 'Invalid input parameters',
                    'status': status.HTTP_400_BAD_REQUEST
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
            # call API for get address
            url = '{url}/channels/{channel}/chaincodes/{chaincode}'.format(url=BARTER_URL, channel=DASH_CHANNEL,
                                                                           chaincode=wallet_name)
            peer = random.choice(DASH_PEERS)
            logger.error('Running action on peer: {}'.format(peer))
            payload = {'peer': peer, 'fcn': 'getFundingAddress', 'args': '["{}"]'.format(wallet_secret)}
            headers = {'Content-Type': 'application/json',
                       'Authorization': 'Bearer {}'.format(token)}
            try:
                r = requests.get(url, headers=headers, params=payload)
                res = r.json()
                data = {
                    'wallet_address': res['address']
                }
            except Exception as e:
                logger.error(e)
                message = "Unknown error"
                if res:
                    message = res['message'] if 'message' in res else 'Unknown error'
                data = {
                    'error': True,
                    'message': message,
                    'status': status.HTTP_400_BAD_REQUEST
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
        elif pid == 'payment_address':
            try:
                wallet_name = input_data['wallet_name']
                wallet_secret = input_data['wallet_secret']
            except Exception as e:
                logger.error(e)
                data = {
                    'error': True,
                    'message': 'Invalid input parameters',
                    'status': status.HTTP_400_BAD_REQUEST
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
            # call API to get payment address
            url = '{url}/channels/{channel}/chaincodes/{chaincode}'.format(url=BARTER_URL, channel=DASH_CHANNEL,
                                                                           chaincode=wallet_name)
            peer = random.choice(DASH_PEERS)
            logger.error('Running action on peer: {}'.format(peer))
            payload = {'peer': peer, 'fcn': 'getPaymentAddress', 'args': '["{}"]'.format(wallet_secret)}
            headers = {'Content-Type': 'application/json',
                       'Authorization': 'Bearer {}'.format(token)}
            try:
                r = requests.get(url, headers=headers, params=payload)
                res = r.json()
                data = {
                    'paymentforward_id': res['paymentforward_id'],
                    'payment_address': res['payment_address'],
                    'destination_address': res['destination_address'],
                    'mining_fee_duffs': res['mining_fee_duffs']
                }
            except Exception as e:
                logger.error(e)
                message = "Unknown error"
                if res:
                    message = res['message'] if 'message' in res else 'Unknown error'
                data = {
                    'error': True,
                    'message': message,
                    'status': status.HTTP_400_BAD_REQUEST
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
        elif pid == 'private_key':
            try:
                wallet_name = input_data['wallet_name']
                wallet_secret = input_data['wallet_secret']
            except Exception as e:
                logger.error(e)
                data = {
                    'error': True,
                    'message': 'Invalid input parameters',
                    'status': status.HTTP_400_BAD_REQUEST
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
            # Call get private key
            url = '{url}/channels/{channel}/chaincodes/{chaincode}'.format(url=BARTER_URL, channel=DASH_CHANNEL,
                                                                           chaincode=wallet_name)
            peer = random.choice(DASH_PEERS)
            logger.error('Running action on peer: {}'.format(peer))
            payload = {'peer': peer, 'fcn': 'getPrivateKey', 'args': '["{}"]'.format(wallet_secret)}
            headers = {'Content-Type': 'application/json',
                       'Authorization': 'Bearer {}'.format(token)}
            try:
                r = requests.get(url, headers=headers, params=payload)
                res = r.json()
                data = {
                    'private_key': res['private_key']
                }
            except Exception as e:
                logger.error(e)
                message = "Unknown error"
                if res:
                    message = res['message'] if 'message' in res else 'Unknown error'
                data = {
                    'error': True,
                    'message': message,
                    'status': status.HTTP_400_BAD_REQUEST
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
        elif pid == 'send_payment':
            try:
                wallet_name = input_data['wallet_name']
                wallet_secret = input_data['wallet_secret']
                destination_address = input_data['destination_address']
                amount_duffs = input_data['amount_duffs']
                instant_send = input_data['instant_send']
            except Exception as e:
                logger.error(e)
                data = {
                    'error': True,
                    'message': 'Invalid input parameters',
                    'status': status.HTTP_400_BAD_REQUEST
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
            # Send payment
            url = '{url}/channels/{channel}/chaincodes/{chaincode}'.format(url=BARTER_URL, channel=DASH_CHANNEL,
                                                                           chaincode=wallet_name)
            peer = random.choice(DASH_PEERS)
            logger.error('Running action on peer: {}'.format(peer))

            payload = {'peer': peer, 'fcn': 'pay',
                       'args': '["{}", "{}", "{}", "{}"]'.format(wallet_secret, destination_address, amount_duffs,
                                                                 instant_send)}
            headers = {'Content-Type': 'application/json',
                       'Authorization': 'Bearer {}'.format(token)}
            try:
                r = requests.get(url, headers=headers, params=payload)
                res = r.json()
                data = {
                    'transaction_id': res['txid']
                }
            except Exception as e:
                logger.error(e)
                message = "Unknown error"
                if res:
                    message = res['message'] if 'message' in res else 'Unknown error'
                data = {
                    'error': True,
                    'message': message,
                    'status': status.HTTP_400_BAD_REQUEST
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
        elif pid == 'ticker':
            try:
                wallet_name = input_data['wallet_name']
            except Exception as e:
                logger.error(e)
                data = {
                    'error': True,
                    'message': 'Invalid input parameters',
                    'status': status.HTTP_400_BAD_REQUEST
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
            # Call get ticker
            url = '{url}/channels/{channel}/chaincodes/{chaincode}'.format(url=BARTER_URL, channel=DASH_CHANNEL,
                                                                           chaincode=wallet_name)
            peer = random.choice(DASH_PEERS)
            logger.error('Running action on peer: {}'.format(peer))

            payload = {'peer': peer, 'fcn': 'ticker', 'args': '[""]'}
            headers = {'Content-Type': 'application/json',
                       'Authorization': 'Bearer {}'.format(token)}
            try:
                r = requests.get(url, headers=headers, params=payload)
                res = r.json()
                data = {
                    'pair': res['message']['pair'],
                    'upper_unix': res['message']['upper_unix'],
                    'lower_unix': res['message']['lower_unix'],
                    'vwap': res['message']['vwap']
                }
            except Exception as e:
                logger.error(e)
                message = "Unknown error"
                if res:
                    message = res['message'] if 'message' in res else 'Unknown error'
                data = {
                    'error': True,
                    'message': message,
                    'status': status.HTTP_400_BAD_REQUEST
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
        return Response(data, status=status.HTTP_200_OK)


class WalletViewBitcoin(APIView):

    def put(self, request, pid):
        input_data = request.data
        if pid not in PID_BITCOIN:
            data = {
                'error': True,
                'message': 'Invalid PID',
                'status': status.HTTP_404_NOT_FOUND
            }
            return Response(data, status=status.HTTP_404_NOT_FOUND)

        if not input_data:
            data = {
                'error': True,
                'message': 'Missing input parameters',
                'status': status.HTTP_400_BAD_REQUEST
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

        # Get authentication token
        token = get_access_token()
        if not token:
            data = {
                'error': True,
                'message': 'Blockchain authentication failed',
                'status': status.HTTP_400_BAD_REQUEST
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        res = dict()

        if pid == 'my_balance':
            try:
                wallet_name = input_data['wallet_name']
                wallet_secret = input_data['wallet_secret']
            except Exception as e:
                logger.error(e)
                data = {
                    'error': True,
                    'message': 'Invalid input parameters',
                    'status': status.HTTP_400_BAD_REQUEST
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
            # call API for wallet balance
            url = '{url}/channels/{channel}/chaincodes/{chaincode}'.format(url=BARTER_URL, channel=BITCOIN_CHANNEL,
                                                                           chaincode=wallet_name)
            peer = random.choice(DASH_PEERS)
            logger.error('Running action on peer: {}'.format(peer))
            payload = {'peer': peer, 'fcn': 'getBalance', 'args': '["{}"]'.format(wallet_secret)}
            headers = {'Content-Type': 'application/json',
                       'Authorization': 'Bearer {}'.format(token)}
            try:
                r = requests.get(url, headers=headers, params=payload)
                res = r.json()
                data = {
                    'wallet_address': res['addrStr'],
                    'balance_bitcoin': res['balance'],
                    'balance_satoshis': res['balanceSat'],
                    'total_received_bitcoin': res['totalReceived'],
                    'total_received_satoshis': res['totalReceivedSat'],
                    'total_sent_bitcoin': res['totalSent'],
                    'total_sent_satoshis': res['totalSentSat'],
                    'unconfirmed_balance_bitcoin': res['unconfirmedBalance'],
                    'unconfirmed_balance_satoshis': res['unconfirmedBalanceSat'],
                    'unconfirmed_appearances': res['unconfirmedTxApperances'],
                    'tx_appearances': res['txApperances']
                }
            except Exception as e:
                logger.error(e)
                message = "Unknown error"
                if res:
                    message = res['message'] if 'message' in res else 'Unknown error'
                data = {
                    'error': True,
                    'message': message,
                    'status': status.HTTP_400_BAD_REQUEST
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
        elif pid == 'my_funding_address':
            try:
                wallet_name = input_data['wallet_name']
                wallet_secret = input_data['wallet_secret']
            except Exception as e:
                logger.error(e)
                data = {
                    'error': True,
                    'message': 'Invalid input parameters',
                    'status': status.HTTP_400_BAD_REQUEST
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
            # call API for get address
            url = '{url}/channels/{channel}/chaincodes/{chaincode}'.format(url=BARTER_URL, channel=BITCOIN_CHANNEL,
                                                                           chaincode=wallet_name)
            peer = random.choice(DASH_PEERS)
            logger.error('Running action on peer: {}'.format(peer))
            payload = {'peer': peer, 'fcn': 'getFundingAddress', 'args': '["{}"]'.format(wallet_secret)}
            headers = {'Content-Type': 'application/json',
                       'Authorization': 'Bearer {}'.format(token)}
            try:
                r = requests.get(url, headers=headers, params=payload)
                res = r.json()
                data = {
                    'wallet_address': res['address']
                }
            except Exception as e:
                logger.error(e)
                message = "Unknown error"
                if res:
                    message = res['message'] if 'message' in res else 'Unknown error'
                data = {
                    'error': True,
                    'message': message,
                    'status': status.HTTP_400_BAD_REQUEST
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
        elif pid == 'payment_address':
            try:
                wallet_name = input_data['wallet_name']
                wallet_secret = input_data['wallet_secret']
            except Exception as e:
                logger.error(e)
                data = {
                    'error': True,
                    'message': 'Invalid input parameters',
                    'status': status.HTTP_400_BAD_REQUEST
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
            # call API to get payment address
            url = '{url}/channels/{channel}/chaincodes/{chaincode}'.format(url=BARTER_URL, channel=BITCOIN_CHANNEL,
                                                                           chaincode=wallet_name)
            peer = random.choice(DASH_PEERS)
            logger.error('Running action on peer: {}'.format(peer))
            payload = {'peer': peer, 'fcn': 'getPaymentAddress', 'args': '["{}"]'.format(wallet_secret)}
            headers = {'Content-Type': 'application/json',
                       'Authorization': 'Bearer {}'.format(token)}
            try:
                r = requests.get(url, headers=headers, params=payload)
                res = r.json()
                data = {
                    'paymentforward_id': res['paymentforward_id'],
                    'payment_address': res['payment_address'],
                    'destination_address': res['destination_address'],
                    'mining_fee_satoshis': res['mining_fee_satoshis']
                }
            except Exception as e:
                logger.error(e)
                message = "Unknown error"
                if res:
                    message = res['message'] if 'message' in res else 'Unknown error'
                data = {
                    'error': True,
                    'message': message,
                    'status': status.HTTP_400_BAD_REQUEST
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
        elif pid == 'private_key':
            try:
                wallet_name = input_data['wallet_name']
                wallet_secret = input_data['wallet_secret']
            except Exception as e:
                logger.error(e)
                data = {
                    'error': True,
                    'message': 'Invalid input parameters',
                    'status': status.HTTP_400_BAD_REQUEST
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
            # Call get private key
            url = '{url}/channels/{channel}/chaincodes/{chaincode}'.format(url=BARTER_URL, channel=BITCOIN_CHANNEL,
                                                                           chaincode=wallet_name)
            peer = random.choice(DASH_PEERS)
            logger.error('Running action on peer: {}'.format(peer))
            payload = {'peer': peer, 'fcn': 'getPrivateKey', 'args': '["{}"]'.format(wallet_secret)}
            headers = {'Content-Type': 'application/json',
                       'Authorization': 'Bearer {}'.format(token)}
            try:
                r = requests.get(url, headers=headers, params=payload)
                res = r.json()
                data = {
                    'private_key': res['private_key']
                }
            except Exception as e:
                logger.error(e)
                message = "Unknown error"
                if res:
                    message = res['message'] if 'message' in res else 'Unknown error'
                data = {
                    'error': True,
                    'message': message,
                    'status': status.HTTP_400_BAD_REQUEST
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
        elif pid == 'send_payment':
            try:
                wallet_name = input_data['wallet_name']
                wallet_secret = input_data['wallet_secret']
                destination_address = input_data['destination_address']
                amount_satoshis = input_data['amount_satoshis']
            except Exception as e:
                logger.error(e)
                data = {
                    'error': True,
                    'message': 'Invalid input parameters',
                    'status': status.HTTP_400_BAD_REQUEST
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
            # Send payment
            url = '{url}/channels/{channel}/chaincodes/{chaincode}'.format(url=BARTER_URL, channel=BITCOIN_CHANNEL,
                                                                           chaincode=wallet_name)
            peer = random.choice(DASH_PEERS)
            logger.error('Running action on peer: {}'.format(peer))
            payload = {'peer': peer, 'fcn': 'pay',
                       'args': '["{}", "{}", "{}"]'.format(wallet_secret, destination_address, amount_satoshis
                                                           )}
            headers = {'Content-Type': 'application/json',
                       'Authorization': 'Bearer {}'.format(token)}
            try:
                r = requests.get(url, headers=headers, params=payload)
                res = r.json()
                data = {
                    'transaction_id': res['txid']
                }
            except Exception as e:
                logger.error(e)
                message = "Unknown error"
                if res:
                    message = res['message'] if 'message' in res else 'Unknown error'
                data = {
                    'error': True,
                    'message': message,
                    'status': status.HTTP_400_BAD_REQUEST
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
        elif pid == 'ticker':
            try:
                wallet_name = input_data['wallet_name']
            except Exception as e:
                logger.error(e)
                data = {
                    'error': True,
                    'message': 'Invalid input parameters',
                    'status': status.HTTP_400_BAD_REQUEST
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
            # Call get ticker
            url = '{url}/channels/{channel}/chaincodes/{chaincode}'.format(url=BARTER_URL, channel=BITCOIN_CHANNEL,
                                                                           chaincode=wallet_name)
            peer = random.choice(DASH_PEERS)
            logger.error('Running action on peer: {}'.format(peer))
            payload = {'peer': peer, 'fcn': 'ticker', 'args': '[""]'}
            headers = {'Content-Type': 'application/json',
                       'Authorization': 'Bearer {}'.format(token)}
            try:
                r = requests.get(url, headers=headers, params=payload)
                res = r.json()
                data = {
                    'pair': res['message']['pair'],
                    'upper_unix': res['message']['upper_unix'],
                    'lower_unix': res['message']['lower_unix'],
                    'vwap': res['message']['vwap']
                }
            except Exception as e:
                logger.error(e)
                message = "Unknown error"
                if res:
                    message = res['message'] if 'message' in res else 'Unknown error'
                data = {
                    'error': True,
                    'message': message,
                    'status': status.HTTP_400_BAD_REQUEST
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
        return Response(data, status=status.HTTP_200_OK)


class RepositoryView(APIView):

    def put(self, request, pid):
        input_data = request.data
        if pid not in PID_REPOSITORY:
            data = {
                'error': True,
                'message': 'Invalid PID',
                'status': status.HTTP_404_NOT_FOUND
            }
            return Response(data, status=status.HTTP_404_NOT_FOUND)

        if not input_data:
            data = {
                'error': True,
                'message': 'Missing input parameters',
                'status': status.HTTP_400_BAD_REQUEST
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

        # Get authentication token
        token = get_access_token()
        if not token:
            data = {
                'error': True,
                'message': 'Blockchain authentication failed',
                'status': status.HTTP_400_BAD_REQUEST
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        res = dict()
        if pid == 'create_asset':
            try:
                repository_name = input_data['repository_name']
                repository_secret = input_data['repository_secret']
                asset_key = input_data['asset_key']
                asset_value = input_data['asset_value']
            except Exception as e:
                logger.error(e)
                data = {
                    'error': True,
                    'message': 'Invalid input parameters',
                    'status': status.HTTP_400_BAD_REQUEST
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
            url = '{url}/channels/{channel}/chaincodes/{chaincode}'.format(url=BARTER_URL, channel=REPOSITORY_CHANNEL,
                                                                           chaincode=repository_name)
            payload = {
                'fcn': 'create',
                'args': [repository_secret, asset_key, asset_value]
            }
            headers = {'Content-Type': 'application/json',
                       'Authorization': 'Bearer {}'.format(token)}
            try:
                r = requests.post(url, headers=headers, data=json.dumps(payload))
                res = r.json()

                if not res['success']:
                    message = res['message']
                    data = {
                        'error': message
                    }
                else:
                    tx_id =res['message'].split(':')[1].strip()
                    data = {
                        'transaction_id': tx_id
                    }
            except Exception as e:
                logger.error(e)
                message = "Unknown error"
                if res:
                    message = res['message'] if 'message' in res else 'Unknown error'
                data = {
                    'error': True,
                    'message': message,
                    'status': status.HTTP_400_BAD_REQUEST
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
        elif pid == 'read_asset_by_key':
            try:
                repository_name = input_data['repository_name']
                repository_secret = input_data['repository_secret']
                asset_key = input_data['asset_key']
            except Exception as e:
                data = {
                    'error': True,
                    'message': 'Invalid input parameters',
                    'status': status.HTTP_400_BAD_REQUEST
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
            url = '{url}/channels/{channel}/chaincodes/{chaincode}'.format(url=BARTER_URL, channel=REPOSITORY_CHANNEL,
                                                                           chaincode=repository_name)
            peer = random.choice(REPOSITORY_PEERS)
            logger.error('Running action on peer: {}'.format(peer))
            payload = {'peer': peer, 'fcn': 'read',
                       'args': '["{}", "{}"]'.format(repository_secret, asset_key)}
            headers = {'Content-Type': 'application/json',
                       'Authorization': 'Bearer {}'.format(token)}
            try:
                r = requests.get(url, headers=headers, params=payload)
                res = r.json()
                if 'message' in res:
                    data = {
                        'error': True,
                        'message': res['message'],
                        'status': status.HTTP_400_BAD_REQUEST
                    }
                    return Response(data, status=status.HTTP_400_BAD_REQUEST)
                else:
                    data = {
                        'asset': res
                    }
            except Exception as e:
                logger.error(e)
                message = "Unknown error"
                if res:
                    message = res['message'] if 'message' in res else 'Unknown error'
                data = {
                    'error': True,
                    'message': message,
                    'status': status.HTTP_400_BAD_REQUEST
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
        elif pid == 'update_asset':
            try:
                repository_name = input_data['repository_name']
                repository_secret = input_data['repository_secret']
                asset_key = input_data['asset_key']
                asset_new_value = input_data['asset_new_value']
            except Exception as e:
                logger.error(e)
                data = {
                    'error': True,
                    'message': 'Invalid input parameters',
                    'status': status.HTTP_400_BAD_REQUEST
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
            url = '{url}/channels/{channel}/chaincodes/{chaincode}'.format(url=BARTER_URL, channel=REPOSITORY_CHANNEL,
                                                                           chaincode=repository_name)
            payload = {'fcn': 'update',
                       'args': [repository_secret, asset_key, asset_new_value]
                       }
            headers = {'Content-Type': 'application/json',
                       'Authorization': 'Bearer {}'.format(token)}
            try:
                r = requests.post(url, headers=headers, data=json.dumps(payload))
                res = r.json()
                data = {
                    'message': res['message']
                }
                if not res['success']:
                    message = res['message']
                    data = {
                        'error': message
                    }
                else:
                    tx_id = res['message'].split(':')[1].strip()
                    data = {
                        'transaction_id': tx_id
                    }
            except Exception as e:
                logger.error(e)
                message = "Unknown error"
                if res:
                    message = res['message'] if 'message' in res else 'Unknown error'
                data = {
                    'error': True,
                    'message': message,
                    'status': status.HTTP_400_BAD_REQUEST
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
        elif pid == 'invalidate_asset':
            try:
                repository_name = input_data['repository_name']
                repository_secret = input_data['repository_secret']
                asset_key = input_data['asset_key']
            except Exception as e:
                logger.error(e)
                data = {
                    'error': True,
                    'message': 'Invalid input parameters',
                    'status': status.HTTP_400_BAD_REQUEST
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
            url = '{url}/channels/{channel}/chaincodes/{chaincode}'.format(url=BARTER_URL, channel=REPOSITORY_CHANNEL,
                                                                           chaincode=repository_name)
            payload = {'fcn': 'delete',
                       'args': [repository_secret, asset_key]
                       }
            headers = {'Content-Type': 'application/json',
                       'Authorization': 'Bearer {}'.format(token)}
            try:
                r = requests.post(url, headers=headers, data=json.dumps(payload))
                res = r.json()
                data = {
                    'message': res['message']
                }
                if not res['success']:
                    message = res['message']
                    data = {
                        'error': message
                    }
                else:
                    tx_id = res['message'].split(':')[1].strip()
                    data = {
                        'transaction_id': tx_id
                    }
            except Exception as e:
                logger.error(e)
                message = "Unknown error"
                if res:
                    message = res['message'] if 'message' in res else 'Unknown error'
                data = {
                    'error': True,
                    'message': message,
                    'status': status.HTTP_400_BAD_REQUEST
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
        elif pid == 'read_assets_by_key_range':
            try:
                repository_name = input_data['repository_name']
                repository_secret = input_data['repository_secret']
                key_from = input_data['key_from']
                key_to = input_data['key_to']
            except Exception as e:
                data = {
                    'error': True,
                    'message': 'Invalid input parameters',
                    'status': status.HTTP_400_BAD_REQUEST
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
            url = '{url}/channels/{channel}/chaincodes/{chaincode}'.format(url=BARTER_URL, channel=REPOSITORY_CHANNEL,
                                                                           chaincode=repository_name)
            peer = random.choice(REPOSITORY_PEERS)
            logger.error('Running action on peer: {}'.format(peer))
            payload = {'peer': peer, 'fcn': 'getAssetByKeyRange',
                       'args': '["{}", "{}", "{}"]'.format(repository_secret, key_from, key_to)}
            headers = {'Content-Type': 'application/json',
                       'Authorization': 'Bearer {}'.format(token)}
            try:
                r = requests.get(url, headers=headers, params=payload)
                res = r.json()

                if 'message' in res:
                    data = {
                        'error': True,
                        'message': res['message'],
                        'status': status.HTTP_400_BAD_REQUEST
                    }
                    return Response(data, status=status.HTTP_400_BAD_REQUEST)
                else:
                    data = {
                        'asset_list': res
                    }
            except Exception as e:
                logger.error(e)
                message = "Unknown error"
                if res:
                    message = res['message'] if 'message' in res else 'Unknown error'
                data = {
                    'error': True,
                    'message': message,
                    'status': status.HTTP_400_BAD_REQUEST
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
        elif pid == 'read_asset_history':
            try:
                repository_name = input_data['repository_name']
                repository_secret = input_data['repository_secret']
                asset_key = input_data['asset_key']
            except Exception as e:
                data = {
                    'error': True,
                    'message': 'Invalid input parameters',
                    'status': status.HTTP_400_BAD_REQUEST
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
            url = '{url}/channels/{channel}/chaincodes/{chaincode}'.format(url=BARTER_URL, channel=REPOSITORY_CHANNEL,
                                                                           chaincode=repository_name)
            peer = random.choice(REPOSITORY_PEERS)
            logger.error('Running action on peer: {}'.format(peer))
            payload = {'peer': peer, 'fcn': 'getHistoryForAsset',
                       'args': '["{}", "{}"]'.format(repository_secret, asset_key)}
            headers = {'Content-Type': 'application/json',
                       'Authorization': 'Bearer {}'.format(token)}
            try:
                r = requests.get(url, headers=headers, params=payload)
                res = r.json()
                data = {
                    'asset_history': res
                }
            except Exception as e:
                logger.error(e)
                message = "Unknown error"
                if res:
                    message = res['message'] if 'message' in res else 'Unknown error'
                data = {
                    'error': True,
                    'message': message,
                    'status': status.HTTP_400_BAD_REQUEST
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
        elif pid == 'couchdb_query_assets':
            try:
                repository_name = input_data['repository_name']
                repository_secret = input_data['repository_secret']
                query = input_data['query']
            except Exception as e:
                logger.error(e)
                data = {
                    'error': True,
                    'message': 'Invalid input parameters',
                    'status': status.HTTP_400_BAD_REQUEST
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
            url = '{url}/channels/{channel}/chaincodes/{chaincode}'.format(url=BARTER_URL, channel=REPOSITORY_CHANNEL,
                                                                           chaincode=repository_name)
            peer = random.choice(REPOSITORY_PEERS)
            logger.error('Running action on peer: {}'.format(peer))
            payload = {'peer': peer, 'fcn': 'queryAssets',
                       'args': '["{}", "{}"]'.format(repository_secret, query.replace('"', '\\"'))}
            logger.error(payload)
            headers = {'Content-Type': 'application/json',
                       'Authorization': 'Bearer {}'.format(token)}
            try:
                r = requests.get(url, headers=headers, params=payload)
                res = r.json()
                data = {
                    'asset_list': res
                }
            except Exception as e:
                logger.error(e)
                message = "Unknown error"
                if res:
                    message = res['message'] if 'message' in res else 'Unknown error'
                data = {
                    'error': True,
                    'message': message,
                    'status': status.HTTP_400_BAD_REQUEST
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
        return Response(data, status=status.HTTP_200_OK)


class WalletEventsSimulation(APIView):
    def get(self, request, iid, oid, eid):
        # Simulate event subscribe
        logger.error(oid)
        logger.error(eid)
        url = 'http://localhost:9997/agent/objects/{oid}/events/{eid}'.format(oid=oid, eid=eid)
        headers = {'infrastructure-id': 'barter-data-storage',
                   'adapter-id': 'barter-test'}
        r = requests.post(url, headers=headers)
        data = {
            'subscribed': True
        }
        return Response(data, status=status.HTTP_200_OK)

    def put(self, request, iid, oid, eid):
        # Simulate event received
        logger.error(iid)
        logger.error(oid)
        logger.error(eid)
        logger.error('Received data:')
        logger.error(request.data)
        return Response({}, status=status.HTTP_200_OK)


class WalletEventsDash(APIView):

    def post(self, request):
        try:
            input_event = request.data
            data = {
                'paymentforward_id': input_event['paymentforward_id'],
                'payment_address': input_event['payment_address'],
                'created_date': input_event['created_date'],
                'received_amount_duffs': input_event['received_amount_duffs'],
                'destination_address': input_event['destination_address'],
                'mining_fee_duffs': input_event['mining_fee_duffs'],
                'input_transaction_id': input_event['input_transaction_hash'],
                'is_instant_send': input_event['input_txlock'],
                'transaction_id': input_event['transaction_hash'],
            }
            url = 'http://localhost:9997/agent/events/{}'.format(DASH_EID)
            headers = {'infrastructure-id': BARTER_DASH_OID, 'adapter-id': ADAPTER_ID}
            r = requests.put(url, data=json.dumps(data), headers=headers)
            logger.error(json.dumps(data))
        except Exception as e:
            logger.error(e)
            return Response({}, status=status.HTTP_400_BAD_REQUEST)
        return Response({}, status=status.HTTP_200_OK)


class WalletEventsBitcoin(APIView):

    def post(self, request):
        try:
            input_event = request.data
            data = {
                'paymentforward_id': input_event['paymentforward_id'],
                'payment_address': input_event['payment_address'],
                'created_date': input_event['created_date'],
                'received_amount_satoshis': input_event['received_amount_satoshis'],
                'destination_address': input_event['destination_address'],
                'mining_fee_satoshis': input_event['mining_fee_satoshis'],
                'input_transaction_id': input_event['input_transaction_hash'],
                'transaction_id': input_event['transaction_hash'],
            }
            url = 'http://localhost:9997/agent/events/{}'.format(BITCOIN_EID)
            headers = {'infrastructure-id': BARTER_BITCOIN_OID, 'adapter-id': ADAPTER_ID}
            r = requests.put(url, data=json.dumps(data), headers=headers)
            logger.error(json.dumps(data))
        except Exception as e:
            logger.error(e)
            return Response({}, status=status.HTTP_400_BAD_REQUEST)
        return Response({}, status=status.HTTP_200_OK)
