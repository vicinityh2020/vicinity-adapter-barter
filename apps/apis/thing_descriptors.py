PID_DASH = ['my_balance', 'my_funding_address', 'payment_address', 'private_key', 'send_payment', 'ticker']

AID_DASH = ['wallet_setup', 'wallet_recover']

PID_BITCOIN = ['my_balance', 'my_funding_address', 'payment_address', 'private_key', 'send_payment', 'ticker']

AID_BITCOIN = ['wallet_setup', 'wallet_recover']

PID_REPOSITORY = ['create_asset', 'read_asset_by_key', 'update_asset', 'invalidate_asset', 'read_assets_by_key_range',
                  'read_asset_history', 'couchdb_query_assets']

AID_REPOSITORY = ['repository_setup']

MY_BALANCE_DASH = {
    "pid": "my_balance",
    "monitors": "adapters:WalletBalance",
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
                    "schema": {
                        "type": "string"
                    }
                },
                {
                    "name": "balance_dash",
                    "schema": {
                        "type": "double"
                    }
                },
                {
                    "name": "balance_duffs",
                    "schema": {
                        "type": "integer"
                    }
                },
                {
                    "name": "total_received_dash",
                    "schema": {
                        "type": "double"
                    }
                },
                {
                    "name": "total_received_duffs",
                    "schema": {
                        "type": "integer"
                    }
                },
                {
                    "name": "total_sent_dash",
                    "schema": {
                        "type": "double"
                    }
                },
                {
                    "name": "total_sent_duffs",
                    "schema": {
                        "type": "integer"
                    }
                },
                {
                    "name": "unconfirmed_balance_dash",
                    "schema": {
                        "type": "double"
                    }
                },
                {
                    "name": "unconfirmed_balance_duffs",
                    "schema": {
                        "type": "integer"
                    }
                },
                {
                    "name": "unconfirmed_appearances",
                    "schema": {
                        "type": "integer"
                    }
                },
                {
                    "name": "tx_appearances",
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
    "monitors": "adapters:WalletBalance",
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
                    "schema": {
                        "type": "string"
                    }
                },
                {
                    "name": "balance_bitcoin",
                    "schema": {
                        "type": "double"
                    }
                },
                {
                    "name": "balance_satoshis",
                    "schema": {
                        "type": "integer"
                    }
                },
                {
                    "name": "total_received_bitcoin",
                    "schema": {
                        "type": "double"
                    }
                },
                {
                    "name": "total_received_satoshis",
                    "schema": {
                        "type": "integer"
                    }
                },
                {
                    "name": "total_sent_bitcoin",
                    "schema": {
                        "type": "double"
                    }
                },
                {
                    "name": "total_sent_satoshis",
                    "schema": {
                        "type": "integer"
                    }
                },
                {
                    "name": "unconfirmed_balance_bitcoin",
                    "schema": {
                        "type": "double"
                    }
                },
                {
                    "name": "unconfirmed_balance_satoshis",
                    "schema": {
                        "type": "integer"
                    }
                },
                {
                    "name": "unconfirmed_appearances",
                    "schema": {
                        "type": "integer"
                    }
                },
                {
                    "name": "tx_appearances",
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
    "monitors": "adapters:WalletFundingAddress",
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
    "monitors": "adapters:WalletFundingAddress",
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
    "monitors": "adapters:WalletPaymentForward",
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
            ]
        }
    }
}

PAYMENT_ADDRESS_BITCOIN = {
    "pid": "payment_address",
    "monitors": "adapters:WalletPaymentForward",
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
                }
            ]
        }
    }
}

TICKER_DASH = {
    "pid": "ticker",
    "monitors": "adapters:WalletValue",
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
                    "schema": {
                        "type": "string"
                    }
                },
                {
                    "name": "upper_unix",
                    "schema": {
                        "type": "integer"
                    }
                },
                {
                    "name": "lower_unix",
                    "schema": {
                        "type": "integer"
                    }
                },
                {
                    "name": "vwap",
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
    "monitors": "adapters:WalletValue",
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
                    "schema": {
                        "type": "string"
                    }
                },
                {
                    "name": "upper_unix",
                    "schema": {
                        "type": "integer"
                    }
                },
                {
                    "name": "lower_unix",
                    "schema": {
                        "type": "integer"
                    }
                },
                {
                    "name": "vwap",
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
    "monitors": "adapters:WalletPrivateKey",
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
    "monitors": "adapters:WalletPrivateKey",
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
    "monitors": "adapters:WalletTransactions",
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
    "monitors": "adapters:WalletTransactions",
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
    "monitors": "adapters:WalletTransactions",
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
            },
            {
                "name": "input_transaction_id",
                "schema": {
                    "type": "string"
                }
            },
            {
                "name": "is_instant_send",
                "schema": {
                    "type": "boolean"
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

BITCOIN_EID = "bitcoin_payments"

PAYMENT_EVENT_BITCOIN = {
    "eid": BITCOIN_EID,
    "monitors": "adapters:WalletTransactions",
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
                },
                {
                    "name": "chainrider_token",
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
                    "schema": {
                        "type": "string"
                    }
                }
            ]
        }
    },
    "affects": "adapters:WalletEntity"
}

ACTION_WALLET_RECOVER_DASH = {
    "aid": "wallet_recover",
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
                },
                {
                    "name": "chainrider_token",
                    "schema": {
                        "type": "string"
                    }
                },
                {
                    "name": "private_key",
                    "schema": {
                        "type": "string"
                    }
                },
            ]
        },
        "output": {
            "type": "object",
            "field": [
                {
                    "name": "wallet_name",
                    "schema": {
                        "type": "string"
                    }
                }
            ]
        }
    },
    "affects": "adapters:WalletEntity"
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
                },
                {
                    "name": "chainrider_token",
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
                    "schema": {
                        "type": "string"
                    }
                }
            ]
        }
    },
    "affects": "adapters:WalletEntity"
}

ACTION_WALLET_RECOVER_BITCOIN = {
    "aid": "wallet_recover",
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
                },
                {
                    "name": "chainrider_token",
                    "schema": {
                        "type": "string"
                    }
                },
                 {
                    "name": "private_key",
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
                    "schema": {
                        "type": "string"
                    }
                }
            ]
        }
    },
    "affects": "adapters:WalletEntity"
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
                    "schema": {
                        "type": "string"
                    }
                }
            ]
        }
    },
    "affects": "adapters:RepositoyEntity"
}

CREATE_ASSET = {
    "pid": "create_asset",
    "monitors": "adapters:RepositoryDigitalAsset",
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
    "monitors": "adapters:RepositoryDigitalAsset",
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
                    "schema": {
                        "type": "object",
                        "field": [
                            {
                                "name": "value",
                                "schema": {
                                    "type": "string"
                                }
                            },
                            {
                                "name": "key",
                                "schema": {
                                    "type": "string"
                                }
                            }
                        ]
                    }
                }
            ]
        }
    }
}

UPDATE_ASSET = {
    "pid": "update_asset",
    "monitors": "adapters:RepositoryDigitalAsset",
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
    "monitors": "adapters:RepositoryDigitalAsset",
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
    "monitors": "adapters:RepositoryDigitalAsset",
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
                    "schema": {
                        "type": "array",
                        "item": {
                            "type": "object",
                            "field": [
                                {
                                    "name": "Record",
                                    "schema": {
                                        "type": "object",
                                        "field": [{
                                            "name": "value",
                                            "schema": {
                                                "type": "string"
                                            }
                                        },
                                            {
                                                "name": "key",
                                                "schema": {
                                                    "type": "string"
                                                }
                                            }
                                        ]
                                    }
                                },
                                {
                                    "name": "Key",
                                    "schema": {
                                        "type": "string"
                                    }
                                }
                            ]
                        }
                    }
                }
            ]
        }
    }
}

READ_ASSET_HISTORY = {
    "pid": "read_asset_history",
    "monitors": "adapters:RepositoryDigitalAsset",
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
                    "schema": {
                        "type": "array",
                        "item": {
                            "type": "object",
                            "field": [
                                {
                                    "name": "TxId",
                                    "schema": {
                                        "type": "string"
                                    }
                                },
                                {
                                    "name": "IsDelete",
                                    "schema": {
                                        "type": "string"
                                    }
                                },
                                {
                                    "name": "Value",
                                    "schema": {
                                        "type": "object",
                                        "field": [{
                                            "name": "value",
                                            "schema": {
                                                "type": "string"
                                            }
                                        },
                                            {
                                                "name": "key",
                                                "schema": {
                                                    "type": "string"
                                                }
                                            }
                                        ]
                                    }
                                },
                                {
                                    "name": "Timestamp",
                                    "schema": {
                                        "type": "object",
                                        "field": [
                                            {
                                                "name": "seconds",
                                                "schema": {
                                                    "type": "object",
                                                    "field": [
                                                        {
                                                            "name": "high",
                                                            "schema": {
                                                                "type": "integer"
                                                            }
                                                        },
                                                        {
                                                            "name": "low",
                                                            "schema": {
                                                                "type": "integer"
                                                            }
                                                        },
                                                        {
                                                            "name": "unsigned",
                                                            "schema": {
                                                                "type": "boolean"
                                                            }
                                                        }
                                                    ]
                                                }
                                            },
                                            {
                                                "name": "nanos",
                                                "schema": {
                                                    "type": "integer"
                                                }
                                            }
                                        ]
                                    }
                                }

                            ]
                        }
                    }
                }
            ]
        }
    }
}

COUCHDB_QUERY_ASSETS = {
    "pid": "couchdb_query_assets",
    "monitors": "adapters:RepositoryDigitalAsset",
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
                    "schema": {
                        "type": "array",
                        "item": {
                            "type": "object",
                            "field": [
                                {
                                    "name": "Record",
                                    "schema": {
                                        "type": "object",
                                        "field": [{
                                            "name": "value",
                                            "schema": {
                                                "type": "string"
                                            }
                                        },
                                            {
                                                "name": "key",
                                                "schema": {
                                                    "type": "string"
                                                }
                                            }
                                        ]
                                    }
                                },
                                {
                                    "name": "Key",
                                    "schema": {
                                        "type": "string"
                                    }
                                }
                            ]
                        }
                    }
                }
            ]
        }
    }
}
