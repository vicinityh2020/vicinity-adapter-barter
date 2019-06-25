import json
from datetime import datetime, timezone, timedelta

import requests
import rest_framework.status as status
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.views import APIView

from .converters import Convert
from .tasks import test

PID = ['my_balance', 'my_funding_address', 'payment_address', 'ticker']

AID = ['wallet_setup']


@csrf_exempt
def view_parking_space(request, oid, pid):
    response = {
        'error': False,
        'oid': oid,
        'message': 'success',
        'status': status.HTTP_200_OK,
        'body': [],
    }
    # conv = Convert()
    # try:
    #     request.data = json.loads(request.body)

    #     parking_slot = ParkingSpace.objects.get(parking_space_id=parking_slot_id)
    #     # control lower boundaries
    #     af = conv.time_to_seconds(parking_slot.available_from)
    #     at = conv.time_to_seconds(parking_slot.available_to)
    #     request.data['from'] = request.data['from'] if request.data['from'] > af \
    #         else af

    #     # control upper boundaries
    #     request.data['to'] = request.data['to'] if request.data['to'] < at \
    #         else at

    #     res_queryset = ParkingReservation.objects.filter(parking_space=parking_slot)

    # except ParkingReservation.DoesNotExist:
    #     response['body'].append({
    #         'start_time': conv.seconds_to_time(request.data['from']),
    #         'end_time': conv.seconds_to_time(request.data['to']),
    #     })

    #     return JsonResponse(data=response, status=status.HTTP_200_OK)

    # except ParkingSpace.DoesNotExist:
    #     response['error'] = True
    #     response['message'] = 'Invalid parking id'
    #     response['status'] = status.HTTP_404_NOT_FOUND
    #     return JsonResponse(data=response, status=status.HTTP_404_NOT_FOUND)

    # if len(res_queryset) == 0:
    #     # no reservations. Return full day!
    #     response['body'].append({
    #         'sensor_id': parking_slot.parking_space_id,
    #         'street_address': 'Mosseveien 18A',
    #         'price_per_minute': 0.11,
    #         'distance_in_km': 0.6,
    #         'start_time': parking_slot.available_from,
    #         'end_time': parking_slot.available_to,
    #     })
    #     return JsonResponse(data=response, status=status.HTTP_200_OK)

    # sorted_queryset = res_queryset.order_by('time_start')

    # min_from = conv.seconds_to_time(request.data['from'])
    # max_to = conv.seconds_to_time(request.data['to'])

    # for entry in sorted_queryset:
    #     if entry.time_start <= min_from <= entry.time_expire:
    #         min_from = entry.time_expire
    #     if entry.time_start <= max_to <= entry.time_expire:
    #         max_to = entry.time_start

    # max_to_seconds = conv.time_to_seconds(max_to)
    # min_from_seconds = conv.time_to_seconds(min_from)

    # if (max_to_seconds - min_from_seconds) < 0:
    #     return JsonResponse(data=response, status=status.HTTP_200_OK)

    # sorted_queryset = sorted_queryset.filter(time_start__gt=min_from, time_expire__lt=max_to)

    # if len(sorted_queryset) == 0:
    #     response['body'].append({
    #         'sensor_id': parking_slot.parking_space_id,
    #         'street_address': 'Mosseveien 18A',
    #         'price_per_minute': 0.11,
    #         'distance_in_km': 0.6,
    #         'start_time': min_from,
    #         'end_time': max_to,
    #     })
    #     return JsonResponse(data=response, status=status.HTTP_200_OK)

    # start = min_from_seconds + 60
    # end = conv.time_to_seconds(sorted_queryset.first().time_start)

    # # at least 2 minutes in between reservations
    # if (end - start) > 120:
    #     response['body'].append({
    #         'sensor_id': parking_slot.parking_space_id,
    #         'street_address': 'Mosseveien 18A',
    #         'price_per_minute': 0.11,
    #         'distance_in_km': 0.6,
    #         'start_time': conv.seconds_to_time(start),
    #         'end_time': conv.seconds_to_time(end - 60),
    #     })

    # res_count = len(sorted_queryset)
    # for i in range(res_count):
    #     start = conv.time_to_seconds(sorted_queryset[i].time_expire)

    #     end = max_to if (i == res_count - 1) else sorted_queryset[i + 1].time_start
    #     end = conv.time_to_seconds(end)

    #     if (end - start) > 120:
    #         response['body'].append({
    #             'sensor_id': parking_slot.parking_space_id,
    #             'street_address': 'Mosseveien 18A',
    #             'price_per_minute': 0.11,
    #             'distance_in_km': 0.6,
    #             'start_time': conv.seconds_to_time(start + 60),
    #             'end_time': conv.seconds_to_time(end - 60),
    #         })

    return JsonResponse(data=response, status=status.HTTP_200_OK)


class ObjectsView(APIView):
    # This needs to be static
    # We will have one service with following properties:
    # getFundingAddress
    # getbalance
    # getPaymentAddress
    # pay
    # ticker
    # And following actions:
    # install and instantiate wallet
    # And following events
    # receivePaymentNotification
    # service_object_descriptor = {
    #     'adapter-id': 'barter-test',
    #     'thing-descriptions': [
    #         {
    #             'oid': 'barter-test-service',
    #             'name': 'VLF Barter Test Adapter',
    #             'type': 'core:Service',
    #             'version': '0.1',
    #             'keywords': [],
    #             'properties': [],
    #             'events': [],
    #             'actions': [{
    #             "aid" : "status",
    #             "read_link" : {
    #                 "output" : {
    #                 "field" : [{
    #                     "schema" : {
    #                     "type" : "string"
    #                     },
    #                     "name" : "taskId"
    #                 }],
    #                 "type" : "object"
    #                 },
    #                 "href" : "/objects/{oid}/actions/{aid}"
    #             },
    #             "affects" : "adapters:DimmingLevel"
    #             }]
    #         },
    #           {
    #             'oid': 'barter-micropayment-service-c',
    #             'name': 'VLF Barter MicroPayment Service',
    #             'type': 'core:Service',
    #             'version': '0.1',
    #             'keywords': ['micropayment', 'dash', 'bitcoin'],
    #             'properties': [
    #                 {
    #                     "pid": "my_balance",
    #                     "monitors": "adapters:Start",
    #                     "read_link": {
    #                         "href": "/wallets/{oid}/property/{pid}",
    #                         "output": {
    #                             "type": "object",
    #                             "field": [
    #                                 {
    #                                     "name": "balance_duffs",
    #                                     "predicate": "core:value",
    #                                     "schema": {
    #                                         "type": "integer"
    #                                     }
    #                                 }
    #                             ]
    #                         }
    #                     }
    #                 },
    #                 {
    #                     "pid": "my_funding_address",
    #                     "monitors": "adapters:Start",
    #                     "read_link": {
    #                         "href": "/wallets/{oid}/property/{pid}",
    #                         "output": {
    #                             "type": "object",
    #                             "field": [
    #                                 {
    #                                     "name": "funding_address",
    #                                     "predicate": "core:value",
    #                                     "schema": {
    #                                         "type": "string"
    #                                     }
    #                                 }
    #                             ]
    #                         }
    #                     }
    #                 },
    #                 {
    #                     "pid": "payment_address",
    #                     "monitors": "adapters:Start",
    #                     "read_link": {
    #                         "href": "/wallets/{oid}/property/{pid}",
    #                         "output": {
    #                             "type": "object",
    #                             "field": [
    #                                 {
    #                                     "name": "payment_address",
    #                                     "predicate": "core:value",
    #                                     "schema": {
    #                                         "type": "string"
    #                                     }
    #                                 },
    #                                 {
    #                                     "name": "amount_duffs",
    #                                     "predicate": "core:value",
    #                                     "schema": {
    #                                         "type": "integer"
    #                                     }
    #                                 },
    #                                 {
    #                                     "name": "event",
    #                                     "predicate": "core:value",
    #                                     "schema": {
    #                                         "type": "string"
    #                                     }
    #                                 },
    #                             ]
    #                         }
    #                     }
    #                 },
    #                 {
    #                     "pid": "ticker",
    #                     "monitors": "adapters:Start",
    #                     "read_link": {
    #                         "href": "/wallets/{oid}/property/{pid}",
    #                         "output": {
    #                             "type": "object",
    #                             "field": [
    #                                 {
    #                                     "name": "value",
    #                                     "predicate": "core:value",
    #                                     "schema": {
    #                                         "type": "integer"
    #                                     }
    #                                 }
    #                             ]
    #                         }
    #                     }
    #                 }
    #             ],
    #             'events': [],
    #             'actions': []
    #         }
    #     ]
    # }

    service_object_descriptor = {
        'adapter-id': 'barter-test',
        'thing-descriptions': [
            {
                'oid': 'barter-test-service',
                'name': 'VLF Barter Test Adapter',
                'type': 'core:Service',
                'version': '0.1',
                'keywords': [],
                'properties': [],
                'events': [],
                'actions': [{
                    "aid": "status",
                    "read_link": {
                        "output": {
                            "field": [{
                                "schema": {
                                    "type": "string"
                                },
                                "name": "taskId"
                            }],
                            "type": "object"
                        },
                        "href": "/objects/{oid}/actions/{aid}"
                    },
                    "affects": "adapters:DimmingLevel"
                }]
            },
            {
                'oid': 'barter-micropayment-service-c',
                'name': 'VLF Barter MicroPayment Service',
                'type': 'core:Service',
                'version': '0.1',
                'keywords': ['micropayment', 'dash', 'bitcoin'],
                'properties': [
                    {
                        "pid": "my_balance",
                        "monitors": "adapters:Start",
                        "write_link": {
                            "href": "/wallets/property/{pid}",
                            "input": {
                                "type": "object",
                                "field": [
                                    {
                                        "name": "wallet_name",
                                        "schema": {
                                            "type": "string"
                                        }
                                    },
                                    {
                                        "name": "wallet_secret",
                                        "schema": {
                                            "type": "string"
                                        }
                                    }
                                ]
                            },
                            "output": {
                                "type": "object",
                                "field": [
                                    {
                                        "name": "balance_duffs",
                                        "predicate": "core:value",
                                        "schema": {
                                            "type": "integer"
                                        }
                                    }
                                ]
                            }
                        }
                    },
                    {
                        "pid": "my_funding_address",
                        "monitors": "adapters:Start",
                        "write_link": {
                            "href": "/wallets/property/{pid}",
                            "input": {
                                "type": "object",
                                "field": [
                                    {
                                        "name": "wallet_name",
                                        "schema": {
                                            "type": "string"
                                        }
                                    },
                                    {
                                        "name": "wallet_secret",
                                        "schema": {
                                            "type": "string"
                                        }
                                    }
                                ]
                            },
                            "output": {
                                "type": "object",
                                "field": [
                                    {
                                        "name": "funding_address",
                                        "predicate": "core:value",
                                        "schema": {
                                            "type": "string"
                                        }
                                    }
                                ]
                            }
                        }
                    },
                    {
                        "pid": "payment_address",
                        "monitors": "adapters:Start",
                        "write_link": {
                            "href": "/wallets/property/{pid}",
                            "input": {
                                "type": "object",
                                "field": [
                                    {
                                        "name": "wallet_name",
                                        "schema": {
                                            "type": "string"
                                        }
                                    },
                                    {
                                        "name": "amount",
                                        "schema": {
                                            "type": "double"
                                        }
                                    }
                                ]
                            },
                            "output": {
                                "type": "object",
                                "field": [
                                    {
                                        "name": "payment_address",
                                        "predicate": "core:value",
                                        "schema": {
                                            "type": "string"
                                        }
                                    },
                                    {
                                        "name": "amount_duffs",
                                        "predicate": "core:value",
                                        "schema": {
                                            "type": "integer"
                                        }
                                    },
                                    {
                                        "name": "event",
                                        "predicate": "core:value",
                                        "schema": {
                                            "type": "string"
                                        }
                                    },
                                ]
                            }
                        }
                    },
                    {
                        "pid": "ticker",
                        "monitors": "adapters:Start",
                        "write_link": {
                            "href": "/wallets/property/{pid}",
                            "input": {
                                "type": "object",
                                "field": [
                                    {
                                        "name": "currency",
                                        "schema": {
                                            "type": "string"
                                        }
                                    }
                                ]
                            },
                            "output": {
                                "type": "object",
                                "field": [
                                    {
                                        "name": "value",
                                        "predicate": "core:value",
                                        "schema": {
                                            "type": "integer"
                                        }
                                    }
                                ]
                            }
                        }
                    }
                ],
                'events': [{
                    "eid": "eid_example",
                    "monitors": "adapters:MeanPowerConsumption",
                    "output": {
                        "type": "object",
                        "field": [
                            {
                                "name": "tx_id",
                                "schema": {
                                    "type": "string"
                                }
                            },
                            {
                                "name": "amount",
                                "schema": {
                                    "type": "integer"
                                }
                            }
                        ]}
                }
                ],
                'actions': [
                    {
                        "aid": "wallet_setup",
                        "write_link": {
                            "href": "/wallets/{oid}/actions/{aid}",
                            "input": {
                                "type": "object",
                                "field": [
                                    {
                                        "name": "network_type",
                                        "description": "Supported types are: 'mainnet' and 'testnet'.",
                                        "schema": {
                                            "type": "string"
                                        }
                                    },
                                    {
                                        "name": "secret",
                                        "schema": {
                                            "type": "string"
                                        }
                                    }
                                ]
                            },
                            "output": {
                                "type": "object",
                                "field": [
                                    {
                                        "name": "wallet_name",
                                        "predicate": "core:value",
                                        "schema": {
                                            "type": "string"
                                        }
                                    }
                                ]
                            }
                        },
                        "affects": "adapters:DimmingLevel"
                    }
                ]
            }
        ]
    }

    def get(self, request):
        return Response(self.service_object_descriptor, status=status.HTTP_200_OK)


class WalletActions(APIView):

    def delete(self, request, oid, aid):
        print(oid)
        print(aid)
        return Response({}, status=status.HTTP_200_OK)

    def post(self, request, oid, aid):
        print(oid)
        print(aid)
        input_data = request.data
        if aid not in AID:
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
                secret = input_data['secret']
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

    def put(self, request, oid, aid):
        # call API for wallet balance
        data = {
            'wallet_name': "MY_UNIQUE_WALLET_RUNNING"
        }
        url = 'http://localhost:9997/agent/actions/{}'.format(aid)
        headers = {'infrastructure-id': 'barter-micropayment-service-c', 'status': 'running',
                   'adapter-id': 'barter-test'}
        r = requests.put(url, data=json.dumps(data), headers=headers)
        # PUT: / actions / {aid}

        import time
        time.sleep(40)
        data = {
            'wallet_name': "MY_UNIQUE_WALLET_FINISHED"
        }
        url = 'http://localhost:9997/agent/actions/{}'.format(aid)
        headers = {'infrastructure-id': 'barter-micropayment-service-b', 'status': 'finished',
                   'adapter-id': 'barter-test'}
        r = requests.put(url, data=json.dumps(data), headers=headers)

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

    def post(self, request, iid, oid, eid):
        # Dynamically open channel
        # url = 'http://localhost:9997/agent/events/{}'.format(eid)
        # headers = {'infrastructure-id': 'barter-micropayment-service-c', 'adapter-id': 'barter-test'}
        # r = requests.post(url, headers=headers)
        # Only simulate event publish/Send data to channel
        data = {
            'tx_id': "TX_ID",
            'amount': 100
        }
        url = 'http://localhost:9997/agent/events/{}'.format(eid)
        headers = {'infrastructure-id': 'barter-micropayment-service-c', 'adapter-id': 'barter-test'}
        r = requests.put(url, data=json.dumps(data), headers=headers)
        return Response(data, status=status.HTTP_200_OK)


class TaskView(APIView):
    def post(self, request):
        print('task received, and celery task is called')
        test.delay()
        data = {'message': 'success'}
        return Response(data, status=status.HTTP_200_OK)

    def put(self, request):
        print('task finished and i received info about that!')
        data = {'message': 'success'}
        return Response(data, status=status.HTTP_200_OK)


class WalletView(APIView):
    def get(self, request, pid):
        if pid not in PID:
            data = {
                'error': True,
                'message': 'Invalid PID',
                'status': status.HTTP_404_NOT_FOUND
            }
            return Response(data, status=status.HTTP_404_NOT_FOUND)

        if pid == 'my_balance':
            # call API for wallet balance
            data = {
                'balance': 10057389
            }
        elif pid == 'my_funding_address':
            # call API for get address
            data = {
                'address': 'CRYPTO_ADDRESS'
            }
        elif pid == 'payment_address':
            # call API to get payment address based on the USD amount
            data = {
                'payment_address': 'PAYMENT_ADDRESS',
                'amount': 108923490,
                'event_id': 'EVENT_ID'
            }
        elif pid == 'ticker':
            data = {
                'value': 10
            }
        return Response(data, status=status.HTTP_200_OK)

    def put(self, request, pid):
        input_data = request.data
        if pid not in PID:
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
                secret = input_data['secret']
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
                secret = input_data['secret']
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
                amount = input_data['amount']
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
        elif pid == 'ticker':
            try:
                currency = input_data['currency']
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


class StatusView(APIView):
    r = {
        'error': False,
        'message': 'success',
        'status': 'OK',
    }

    def post(self, request):
        return Response(self.r, status=status.HTTP_200_OK)
