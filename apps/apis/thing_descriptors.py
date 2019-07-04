PID_DASH = ['my_balance', 'my_funding_address', 'payment_address', 'private_key', 'send_payment', 'ticker']

AID_DASH = ['wallet_setup']

PID_BITCOIN = ['my_balance', 'my_funding_address', 'payment_address', 'private_key', 'send_payment', 'ticker']

AID_BITCOIN = ['wallet_setup']

PID_REPOSITORY = ['create_asset', 'read_asset_by_key', 'update_asset', 'invalidate_asset', 'read_assets_by_key_range',
                  'read_asset_history', 'couchdb_query_assets']

AID_REPOSITORY = ['repository_setup']

MY_BALANCE_DASH = {
    "pid": "my_balance",
    "monitors": "adapters:Start",
    "write_link": {
        "href": "/wallets/dash/property/{pid}",
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
                    "name": "wallet_address",
                    "predicate": "core:value",
                    "schema": {
                        "type": "string"
                    }
                },
                {
                    "name": "balance_dash",
                    "predicate": "core:value",
                    "schema": {
                        "type": "double"
                    }
                },
                {
                    "name": "balance_duffs",
                    "predicate": "core:value",
                    "schema": {
                        "type": "integer"
                    }
                },
                {
                    "name": "total_received_dash",
                    "predicate": "core:value",
                    "schema": {
                        "type": "double"
                    }
                },
                {
                    "name": "total_received_duffs",
                    "predicate": "core:value",
                    "schema": {
                        "type": "integer"
                    }
                },
                {
                    "name": "total_sent_dash",
                    "predicate": "core:value",
                    "schema": {
                        "type": "double"
                    }
                },
                {
                    "name": "total_sent_duffs",
                    "predicate": "core:value",
                    "schema": {
                        "type": "integer"
                    }
                },
                {
                    "name": "unconfirmed_balance_dash",
                    "predicate": "core:value",
                    "schema": {
                        "type": "double"
                    }
                },
                {
                    "name": "unconfirmed_balance_duffs",
                    "predicate": "core:value",
                    "schema": {
                        "type": "integer"
                    }
                },
                {
                    "name": "unconfirmed_appearances",
                    "predicate": "core:value",
                    "schema": {
                        "type": "integer"
                    }
                },
                {
                    "name": "tx_appearances",
                    "predicate": "core:value",
                    "schema": {
                        "type": "integer"
                    }
                }
            ]
        }
    }
}

MY_BALANCE_BITCOIN = {
    "pid": "my_balance",
    "monitors": "adapters:Start",
    "write_link": {
        "href": "/wallets/bitcoin/property/{pid}",
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
                    "name": "wallet_address",
                    "predicate": "core:value",
                    "schema": {
                        "type": "string"
                    }
                },
                {
                    "name": "balance_bitcoin",
                    "predicate": "core:value",
                    "schema": {
                        "type": "double"
                    }
                },
                {
                    "name": "balance_satoshis",
                    "predicate": "core:value",
                    "schema": {
                        "type": "integer"
                    }
                },
                {
                    "name": "total_received_bitcoin",
                    "predicate": "core:value",
                    "schema": {
                        "type": "double"
                    }
                },
                {
                    "name": "total_received_satoshis",
                    "predicate": "core:value",
                    "schema": {
                        "type": "integer"
                    }
                },
                {
                    "name": "total_sent_bitcoin",
                    "predicate": "core:value",
                    "schema": {
                        "type": "double"
                    }
                },
                {
                    "name": "total_sent_satoshis",
                    "predicate": "core:value",
                    "schema": {
                        "type": "integer"
                    }
                },
                {
                    "name": "unconfirmed_balance_bitcoin",
                    "predicate": "core:value",
                    "schema": {
                        "type": "double"
                    }
                },
                {
                    "name": "unconfirmed_balance_satoshis",
                    "predicate": "core:value",
                    "schema": {
                        "type": "integer"
                    }
                },
                {
                    "name": "unconfirmed_appearances",
                    "predicate": "core:value",
                    "schema": {
                        "type": "integer"
                    }
                },
                {
                    "name": "tx_appearances",
                    "predicate": "core:value",
                    "schema": {
                        "type": "integer"
                    }
                }
            ]
        }
    }
}

MY_FUNDING_ADDRESS_DASH = {
    "pid": "my_funding_address",
    "monitors": "adapters:Start",
    "write_link": {
        "href": "/wallets/dash/property/{pid}",
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
                    "name": "wallet_address",
                    "predicate": "core:value",
                    "schema": {
                        "type": "string"
                    }
                }
            ]
        }
    }
}

MY_FUNDING_ADDRESS_BITCOIN = {
    "pid": "my_funding_address",
    "monitors": "adapters:Start",
    "write_link": {
        "href": "/wallets/bitcoin/property/{pid}",
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
                    "name": "wallet_address",
                    "predicate": "core:value",
                    "schema": {
                        "type": "string"
                    }
                }
            ]
        }
    }
}

PAYMENT_ADDRESS_DASH = {
    "pid": "payment_address",
    "monitors": "adapters:Start",
    "write_link": {
        "href": "/wallets/dash/property/{pid}",
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
                    "name": "paymentforward_id",
                    "predicate": "core:value",
                    "schema": {
                        "type": "string"
                    }
                },
                {
                    "name": "payment_address",
                    "predicate": "core:value",
                    "schema": {
                        "type": "string"
                    }
                },
                {
                    "name": "destination_address",
                    "predicate": "core:value",
                    "schema": {
                        "type": "string"
                    }
                },
                {
                    "name": "mining_fee_duffs",
                    "predicate": "core:value",
                    "schema": {
                        "type": "integer"
                    }
                }
            ]
        }
    }
}

PAYMENT_ADDRESS_BITCOIN = {
    "pid": "payment_address",
    "monitors": "adapters:Start",
    "write_link": {
        "href": "/wallets/bitcoin/property/{pid}",
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
                    "name": "paymentforward_id",
                    "predicate": "core:value",
                    "schema": {
                        "type": "string"
                    }
                },
                {
                    "name": "payment_address",
                    "predicate": "core:value",
                    "schema": {
                        "type": "string"
                    }
                },
                {
                    "name": "destination_address",
                    "predicate": "core:value",
                    "schema": {
                        "type": "string"
                    }
                },
                {
                    "name": "mining_fee_satoshis",
                    "predicate": "core:value",
                    "schema": {
                        "type": "integer"
                    }
                }
            ]
        }
    }
}

TICKER_DASH = {
    "pid": "ticker",
    "monitors": "adapters:Start",
    "write_link": {
        "href": "/wallets/dash/property/{pid}",
        "input": {
            "type": "object",
            "field": [
                {
                    "name": "wallet_name",
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
                    "name": "pair",
                    "predicate": "core:value",
                    "schema": {
                        "type": "string"
                    }
                },
                {
                    "name": "upper_unix",
                    "predicate": "core:value",
                    "schema": {
                        "type": "integer"
                    }
                },
                {
                    "name": "lower_unix",
                    "predicate": "core:value",
                    "schema": {
                        "type": "integer"
                    }
                },
                {
                    "name": "vwap",
                    "predicate": "core:value",
                    "schema": {
                        "type": "string"
                    }
                }
            ]
        }
    }
}

TICKER_BITCOIN = {
    "pid": "ticker",
    "monitors": "adapters:Start",
    "write_link": {
        "href": "/wallets/bitcoin/property/{pid}",
        "input": {
            "type": "object",
            "field": [
                {
                    "name": "wallet_name",
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
                    "name": "pair",
                    "predicate": "core:value",
                    "schema": {
                        "type": "string"
                    }
                },
                {
                    "name": "upper_unix",
                    "predicate": "core:value",
                    "schema": {
                        "type": "integer"
                    }
                },
                {
                    "name": "lower_unix",
                    "predicate": "core:value",
                    "schema": {
                        "type": "integer"
                    }
                },
                {
                    "name": "vwap",
                    "predicate": "core:value",
                    "schema": {
                        "type": "string"
                    }
                }
            ]
        }
    }
}

PRIVATE_KEY_DASH = {
    "pid": "private_key",
    "monitors": "adapters:Start",
    "write_link": {
        "href": "/wallets/dash/property/{pid}",
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
                    "name": "private_key",
                    "predicate": "core:value",
                    "schema": {
                        "type": "string"
                    }
                }
            ]
        }
    }
}

PRIVATE_KEY_BITCOIN = {
    "pid": "private_key",
    "monitors": "adapters:Start",
    "write_link": {
        "href": "/wallets/bitcoin/property/{pid}",
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
                    "name": "private_key",
                    "predicate": "core:value",
                    "schema": {
                        "type": "string"
                    }
                }
            ]
        }
    }
}

SEND_PAYMENT_DASH = {
    "pid": "send_payment",
    "monitors": "adapters:Start",
    "write_link": {
        "href": "/wallets/dash/property/{pid}",
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
                },
                {
                    "name": "destination_address",
                    "schema": {
                        "type": "string"
                    }
                },
                {
                    "name": "amount_duffs",
                    "schema": {
                        "type": "integer"
                    }
                },
                {
                    "name": "instant_send",
                    "schema": {
                        "type": "boolean"
                    }
                }
            ]
        },
        "output": {
            "type": "object",
            "field": [
                {
                    "name": "transaction_id",
                    "predicate": "core:value",
                    "schema": {
                        "type": "string"
                    }
                }
            ]
        }
    }
}

SEND_PAYMENT_BITCOIN = {
    "pid": "send_payment",
    "monitors": "adapters:Start",
    "write_link": {
        "href": "/wallets/bitcoin/property/{pid}",
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
                },
                {
                    "name": "destination_address",
                    "schema": {
                        "type": "string"
                    }
                },
                {
                    "name": "amount_satoshis",
                    "schema": {
                        "type": "integer"
                    }
                }
            ]
        },
        "output": {
            "type": "object",
            "field": [
                {
                    "name": "transaction_id",
                    "predicate": "core:value",
                    "schema": {
                        "type": "string"
                    }
                }
            ]
        }
    }
}

DASH_EID = "dash_payments"
PAYMENT_EVENT_DASH = {
    "eid": DASH_EID,
    "monitors": "adapters:MeanPowerConsumption",
    "output": {
        "type": "object",
        "field": [
            {
                "name": "paymentforward_id",
                "schema": {
                    "type": "string"
                }
            },
            {
                "name": "payment_address",
                "schema": {
                    "type": "string"
                }
            },
            {
                "name": "created_date",
                "schema": {
                    "type": "string"
                }
            },
            {
                "name": "received_amount_duffs",
                "schema": {
                    "type": "integer"
                }
            },
            {
                "name": "destination_address",
                "schema": {
                    "type": "string"
                }
            },
            {
                "name": "mining_fee_duffs",
                "schema": {
                    "type": "integer"
                }
            }
            ,
            {
                "name": "input_transaction_id",
                "schema": {
                    "type": "string"
                }
            }
            ,
            {
                "name": "is_instant_send",
                "schema": {
                    "type": "boolean"
                }
            }
            ,
            {
                "name": "transaction_id",
                "schema": {
                    "type": "string"
                }
            }
        ]}
}


BITCOIN_EID = "bitcoin_payments"

PAYMENT_EVENT_BITCOIN = {
    "eid": BITCOIN_EID,
    "monitors": "adapters:MeanPowerConsumption",
    "output": {
        "type": "object",
        "field": [
            {
                "name": "paymentforward_id",
                "schema": {
                    "type": "string"
                }
            },
            {
                "name": "payment_address",
                "schema": {
                    "type": "string"
                }
            },
            {
                "name": "created_date",
                "schema": {
                    "type": "string"
                }
            },
            {
                "name": "received_amount_satoshis",
                "schema": {
                    "type": "integer"
                }
            },
            {
                "name": "destination_address",
                "schema": {
                    "type": "string"
                }
            },
            {
                "name": "mining_fee_satoshis",
                "schema": {
                    "type": "integer"
                }
            },
            {
                "name": "input_transaction_id",
                "schema": {
                    "type": "string"
                }
            },
            {
                "name": "transaction_id",
                "schema": {
                    "type": "string"
                }
            }
        ]}
}

ACTION_WALLET_SETUP_DASH = {
    "aid": "wallet_setup",
    "write_link": {
        "href": "/wallets/dash/{oid}/actions/{aid}",
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

ACTION_WALLET_SETUP_BITCOIN = {
    "aid": "wallet_setup",
    "write_link": {
        "href": "/wallets/bitcoin/{oid}/actions/{aid}",
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

SETUP_REPOSITORY = {
    "aid": "repository_setup",
    "write_link": {
        "href": "/repositories/{oid}/actions/{aid}",
        "input": {
            "type": "object",
            "field": [
                {
                    "name": "repository_secret",
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
                    "name": "repository_name",
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

CREATE_ASSET = {
    "pid": "create_asset",
    "monitors": "adapters:Start",
    "write_link": {
        "href": "/repositories/property/{pid}",
        "input": {
            "type": "object",
            "field": [
                {
                    "name": "repository_name",
                    "schema": {
                        "type": "string"
                    }
                },
                {
                    "name": "repository_secret",
                    "schema": {
                        "type": "string"
                    }
                },
                {
                    "name": "asset_key",
                    "schema": {
                        "type": "string"
                    }
                },
                {
                    "name": "asset_value",
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
                    "name": "transaction_id",
                    "predicate": "core:value",
                    "schema": {
                        "type": "string"
                    }
                }
            ]
        }
    }
}

READ_ASSET_BY_KEY = {
    "pid": "read_asset_by_key",
    "monitors": "adapters:Start",
    "write_link": {
        "href": "/repositories/property/{pid}",
        "input": {
            "type": "object",
            "field": [
                {
                    "name": "repository_name",
                    "schema": {
                        "type": "string"
                    }
                },
                {
                    "name": "repository_secret",
                    "schema": {
                        "type": "string"
                    }
                },
                {
                    "name": "asset_key",
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
                    "name": "asset",
                    "predicate": "core:value",
                    "schema": {
                        "type": "string"
                    }
                }
            ]
        }
    }
}

UPDATE_ASSET = {
    "pid": "update_asset",
    "monitors": "adapters:Start",
    "write_link": {
        "href": "/repositories/property/{pid}",
        "input": {
            "type": "object",
            "field": [
                {
                    "name": "repository_name",
                    "schema": {
                        "type": "string"
                    }
                },
                {
                    "name": "repository_secret",
                    "schema": {
                        "type": "string"
                    }
                },
                {
                    "name": "asset_key",
                    "schema": {
                        "type": "string"
                    }
                },
                {
                    "name": "asset_new_value",
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
                    "name": "transaction_id",
                    "predicate": "core:value",
                    "schema": {
                        "type": "string"
                    }
                }
            ]
        }
    }
}

INVALIDATE_ASSET = {
    "pid": "invalidate_asset",
    "monitors": "adapters:Start",
    "write_link": {
        "href": "/repositories/property/{pid}",
        "input": {
            "type": "object",
            "field": [
                {
                    "name": "repository_name",
                    "schema": {
                        "type": "string"
                    }
                },
                {
                    "name": "repository_secret",
                    "schema": {
                        "type": "string"
                    }
                },
                {
                    "name": "asset_key",
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
                    "name": "transaction_id",
                    "predicate": "core:value",
                    "schema": {
                        "type": "string"
                    }
                }
            ]
        }
    }
}

READ_ASSETS_BY_KEY_RANGE = {
    "pid": "read_assets_by_key_range",
    "monitors": "adapters:Start",
    "write_link": {
        "href": "/repositories/property/{pid}",
        "input": {
            "type": "object",
            "field": [
                {
                    "name": "repository_name",
                    "schema": {
                        "type": "string"
                    }
                },
                {
                    "name": "repository_secret",
                    "schema": {
                        "type": "string"
                    }
                },
                {
                    "name": "key_from",
                    "schema": {
                        "type": "string"
                    }
                },
                {
                    "name": "key_to",
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
                    "name": "asset_list",
                    "predicate": "core:value",
                    "schema": {
                        "type": "string"
                    }
                }
            ]
        }
    }
}

READ_ASSET_HISTORY = {
    "pid": "read_asset_history",
    "monitors": "adapters:Start",
    "write_link": {
        "href": "/repositories/property/{pid}",
        "input": {
            "type": "object",
            "field": [
                {
                    "name": "repository_name",
                    "schema": {
                        "type": "string"
                    }
                },
                {
                    "name": "repository_secret",
                    "schema": {
                        "type": "string"
                    }
                },
                {
                    "name": "asset_key",
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
                    "name": "asset_history",
                    "predicate": "core:value",
                    "schema": {
                        "type": "string"
                    }
                }
            ]
        }
    }
}

COUCHDB_QUERY_ASSETS = {
    "pid": "couchdb_query_assets",
    "monitors": "adapters:Start",
    "write_link": {
        "href": "/repositories/property/{pid}",
        "input": {
            "type": "object",
            "field": [
                {
                    "name": "repository_name",
                    "schema": {
                        "type": "string"
                    }
                },
                {
                    "name": "repository_secret",
                    "schema": {
                        "type": "string"
                    }
                },
                {
                    "name": "query",
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
                    "name": "asset_list",
                    "predicate": "core:value",
                    "schema": {
                        "type": "string"
                    }
                }
            ]
        }
    }
}
