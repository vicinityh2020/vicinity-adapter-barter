import json
from datetime import datetime, timezone, timedelta

import requests
import rest_framework.status as status
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView

from .tasks import test
from .thing_descriptors import *


class ObjectsView(APIView):
    service_object_descriptor = {
        'adapter-id': 'barter-test',
        'thing-descriptions': [
            {
                'oid': 'barter-micropayment-dash',
                'name': 'VLF Barter MicroPayment Service based on DASH cryptocurrency',
                'type': 'core:Service',
                'version': '0.1',
                'keywords': ['micropayment', 'dash', 'wallet'],
                'properties': [MY_BALANCE_DASH, MY_FUNDING_ADDRESS_DASH, PAYMENT_ADDRESS_DASH, TICKER_DASH,
                               PRIVATE_KEY_DASH, SEND_PAYMENT_DASH],
                'events': [PAYMENT_EVENT_DASH],
                'actions': [ACTION_WALLET_SETUP_DASH]
            },
            {
                'oid': 'barter-micropayment-bitcoin',
                'name': 'VLF Barter MicroPayment Service based on BITCOIN cryptocurrency',
                'type': 'core:Service',
                'version': '0.1',
                'keywords': ['micropayment', 'bitcoin', 'wallet'],
                'properties': [MY_BALANCE_BITCOIN, MY_FUNDING_ADDRESS_BITCOIN, PAYMENT_ADDRESS_BITCOIN, TICKER_BITCOIN,
                               PRIVATE_KEY_BITCOIN, SEND_PAYMENT_BITCOIN],
                'events': [PAYMENT_EVENT_BITCOIN],
                'actions': [ACTION_WALLET_SETUP_BITCOIN]
            },
            {
                'oid': 'barter-data-storage',
                'name': 'VLF Barter Service for data management on permissioned blockchain',
                'type': 'core:Service',
                'version': '0.1',
                'keywords': ['data', 'repository'],
                'properties': [CREATE_ASSET, READ_ASSET_BY_KEY, UPDATE_ASSET, INVALIDATE_ASSET,
                               READ_ASSETS_BY_KEY_RANGE, READ_ASSET_HISTORY],
                'actions': [SETUP_REPOSITORY]
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
                'error': True,
                'message': 'Missing input parameters',
                'status': status.HTTP_400_BAD_REQUEST
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

        if aid == 'wallet_setup':
            try:
                network_type = input_data['network_type']
                wallet_secret = input_data['wallet_secret']
            except Exception as e:
                data = {
                    'error': True,
                    'message': 'Invalid input parameters',
                    'status': status.HTTP_400_BAD_REQUEST
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
            if network_type not in ['mainnet', 'testnet']:
                data = {
                    'error': True,
                    'message': 'Network type must be mainnet or testnet',
                    'status': status.HTTP_400_BAD_REQUEST
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)

            # # call celery task for wallet setup

        data = {}

        return Response(data, status=status.HTTP_200_OK)


class WalletActionsBitcoin(APIView):

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
                'error': True,
                'message': 'Missing input parameters',
                'status': status.HTTP_400_BAD_REQUEST
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

        if aid == 'wallet_setup':
            try:
                network_type = input_data['network_type']
                wallet_secret = input_data['wallet_secret']
            except Exception as e:
                data = {
                    'error': True,
                    'message': 'Invalid input parameters',
                    'status': status.HTTP_400_BAD_REQUEST
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
            if network_type not in ['mainnet', 'testnet']:
                data = {
                    'error': True,
                    'message': 'Network type must be mainnet or testnet',
                    'status': status.HTTP_400_BAD_REQUEST
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)

            # # call celery task for wallet setup

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
                return Response(data, status=status.HTTP_400_BAD_REQUEST)

            # # call celery task for wallet setup

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

        if pid == 'my_balance':
            try:
                wallet_name = input_data['wallet_name']
                wallet_secret = input_data['wallet_secret']
            except Exception as e:
                data = {
                    'error': True,
                    'message': 'Invalid input parameters',
                    'status': status.HTTP_400_BAD_REQUEST
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
            # call API for wallet balance
            data = {
                'balance': 10057389
            }
        elif pid == 'my_funding_address':
            try:
                wallet_name = input_data['wallet_name']
                wallet_secret = input_data['wallet_secret']
            except Exception as e:
                data = {
                    'error': True,
                    'message': 'Invalid input parameters',
                    'status': status.HTTP_400_BAD_REQUEST
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
            # call API for get address
            data = {
                'address': 'CRYPTO_ADDRESS'
            }
        elif pid == 'payment_address':
            try:
                wallet_name = input_data['wallet_name']
                wallet_secret = input_data['wallet_secret']
            except Exception as e:
                data = {
                    'error': True,
                    'message': 'Invalid input parameters',
                    'status': status.HTTP_400_BAD_REQUEST
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
            # call API to get payment address based on the USD amount
            data = {
                'payment_address': 'PAYMENT_ADDRESS',
                'amount': 108923490,
                'event_id': 'EVENT_ID'
            }
        elif pid == 'private_key':
            try:
                wallet_name = input_data['wallet_name']
                wallet_secret = input_data['wallet_secret']
            except Exception as e:
                data = {
                    'error': True,
                    'message': 'Invalid input parameters',
                    'status': status.HTTP_400_BAD_REQUEST
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
            data = {
                'value': 10
            }
        elif pid == 'send_payment':
            try:
                wallet_name = input_data['wallet_name']
                wallet_secret = input_data['wallet_secret']
                destination_address = input_data['destination_address']
                amount_duffs = input_data['amount_satoshis']
            except Exception as e:
                data = {
                    'error': True,
                    'message': 'Invalid input parameters',
                    'status': status.HTTP_400_BAD_REQUEST
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
            data = {
                'value': 10
            }
        elif pid == 'ticker':
            try:
                wallet_name = input_data['wallet_name']
            except Exception as e:
                data = {
                    'error': True,
                    'message': 'Invalid input parameters',
                    'status': status.HTTP_400_BAD_REQUEST
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
            data = {
                'value': 10
            }
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

        if pid == 'my_balance':
            try:
                wallet_name = input_data['wallet_name']
                wallet_secret = input_data['wallet_secret']
            except Exception as e:
                data = {
                    'error': True,
                    'message': 'Invalid input parameters',
                    'status': status.HTTP_400_BAD_REQUEST
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
            # call API for wallet balance
            data = {
                'balance': 10057389
            }
        elif pid == 'my_funding_address':
            try:
                wallet_name = input_data['wallet_name']
                wallet_secret = input_data['wallet_secret']
            except Exception as e:
                data = {
                    'error': True,
                    'message': 'Invalid input parameters',
                    'status': status.HTTP_400_BAD_REQUEST
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
            # call API for get address
            data = {
                'address': 'CRYPTO_ADDRESS'
            }
        elif pid == 'payment_address':
            try:
                wallet_name = input_data['wallet_name']
                wallet_secret = input_data['wallet_secret']
            except Exception as e:
                data = {
                    'error': True,
                    'message': 'Invalid input parameters',
                    'status': status.HTTP_400_BAD_REQUEST
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
            # call API to get payment address based on the USD amount
            data = {
                'payment_address': 'PAYMENT_ADDRESS',
                'amount': 108923490,
                'event_id': 'EVENT_ID'
            }
        elif pid == 'private_key':
            try:
                wallet_name = input_data['wallet_name']
                wallet_secret = input_data['wallet_secret']
            except Exception as e:
                data = {
                    'error': True,
                    'message': 'Invalid input parameters',
                    'status': status.HTTP_400_BAD_REQUEST
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
            data = {
                'value': 10
            }
        elif pid == 'send_payment':
            try:
                wallet_name = input_data['wallet_name']
                wallet_secret = input_data['wallet_secret']
                destination_address = input_data['destination_address']
                amount_duffs = input_data['amount_duffs']
                instant_send = input_data['instant_send']
            except Exception as e:
                data = {
                    'error': True,
                    'message': 'Invalid input parameters',
                    'status': status.HTTP_400_BAD_REQUEST
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
            data = {
                'value': 10
            }
        elif pid == 'ticker':
            try:
                wallet_name = input_data['wallet_name']
            except Exception as e:
                data = {
                    'error': True,
                    'message': 'Invalid input parameters',
                    'status': status.HTTP_400_BAD_REQUEST
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
            data = {
                'value': 10
            }
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

        if pid == 'create_asset':
            try:
                repository_name = input_data['repository_name']
                repository_secret = input_data['repository_secret']
                asset_key = input_data['asset_key']
                asset_value = input_data['asset_value']
            except Exception as e:
                data = {
                    'error': True,
                    'message': 'Invalid input parameters',
                    'status': status.HTTP_400_BAD_REQUEST
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
            # call API for wallet balance
            data = {
                'balance': 10057389
            }
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
            # call API for get address
            data = {
                'address': 'CRYPTO_ADDRESS'
            }
        elif pid == 'update_asset':
            try:
                repository_name = input_data['repository_name']
                repository_secret = input_data['repository_secret']
                asset_key = input_data['asset_key']
                asset_new_value = input_data['asset_new_value']
            except Exception as e:
                data = {
                    'error': True,
                    'message': 'Invalid input parameters',
                    'status': status.HTTP_400_BAD_REQUEST
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
            # call API to get payment address based on the USD amount
            data = {
                'payment_address': 'PAYMENT_ADDRESS',
                'amount': 108923490,
                'event_id': 'EVENT_ID'
            }
        elif pid == 'invalidate_asset':
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
            data = {
                'value': 10
            }
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
            data = {
                'value': 10
            }
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
            data = {
                'value': 10
            }
        elif pid == 'couchdb_query_assets':
            try:
                repository_name = input_data['repository_name']
                repository_secret = input_data['repository_secret']
                query = input_data['query']
            except Exception as e:
                data = {
                    'error': True,
                    'message': 'Invalid input parameters',
                    'status': status.HTTP_400_BAD_REQUEST
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
            data = {
                'value': 10
            }
        return Response(data, status=status.HTTP_200_OK)


class WalletEvents(APIView):
    def get(self, request, iid, oid, eid):
        # Simulate event subscribe
        print(oid)
        print(eid)
        url = 'http://localhost:9997/agent/objects/{oid}/events/{eid}'.format(oid=oid, eid=eid)
        headers = {'infrastructure-id': 'barter-test-service',
                   'adapter-id': 'barter-test'}
        r = requests.post(url, headers=headers)
        data = {
            'subscribed': True
        }
        return Response(data, status=status.HTTP_200_OK)

    def put(self, request, iid, oid, eid):
        # Simulate event received
        print(iid)
        print(oid)
        print(eid)
        print('Received data:')
        print(request.data)
        return Response({}, status=status.HTTP_200_OK)
