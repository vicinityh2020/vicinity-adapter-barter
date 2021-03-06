# About

BARTER is a blockchain framework built on top of open source projects Hyperledger Fabric, Dash and Bitcoin and proprietary VizLore’s [ChainRider service](https://chainrider.io/). It is a micro-payment enabler service that can be exploited to support a range of use-cases that need a secure and scalable M2M micro-payment solution specifically designed for IoT ecosystem. Hyperledger Fabric is an open source enterprise-grade permissioned distributed ledger technology (DLT) platform. ChainRider offers an ecosystem of tools and services built around public and private blockchain which helps in prototyping and building proprietary applications on different blockchains. BARTER integrates all of the aforementioned solutions to provide a private blockchain infrastructure for blockchain-assisted micro-payments, private data storage and smart contracts management. BARTER is a decentralized private blockchain infrastructure with deployed smart contracts for automated micro-payments and data storage, allowing autonomous interaction between IoT ecosystem entities in carrying out everyday business workflows. Regulations, ethics, and business rules can be incorporated through smart contracts, which are stored on BARTER’s Hyperledger blockchain and provide REST API interface for integration with IoT devices in a secure manner. This increases the security of M2M transactions and enforces contract performance. 

![BARTER Architecture](BARTER_architecture.png)

The figure above provides detailed BARTER framework architecture.

# Installation and configuration

BARTER adapter is not meant to be installed by individual users. Instead, VizLore operates the BARTER blockchain infrastructure and exposes the BARTER adapter to the Vicinity ecosystem. 

In order to run BARTER adapter, in addition to starting VICINITY gateway API and configured VICINITY agent following requirements need to be fulfilled:
1. Installing python 3.6
2. Installing and setting up the Postgres database. The info about the name of the database, user, and password could be found in the .env.example file (DATABASE_URL environment variable)
3. Installing requirements by running following command from the root folder of the adapter:
`pip install -r requirements.txt`
4. Managing migrations (run commands from the root folder of the adapter)
`python manage.py makemigrations` `python mamange.py migrate` 
5. Starting the BARTER adapter by running following command from the root folder of the BARTER adapter (it starts the Python Django web application)
`python manage.py runserver 0.0.0.0:8000`
6. Installing redis server.
6. Starting the Celery application which handles actions/tasks within the BARTER framework by running the following command from the root folder of the BARTER adapter
`celery worker -A config --loglevel=info`

# Adapter description

BARTER adapter is publicly available to the Vicinity ecosystem. BARTER adapter exposes three public services:
1. Dash micropayment service
2. Bitcoin micropayment service
3. Repository service

### Dash micropayment service

Dash micropayment service exposes the following:
* Actions
  * wallet_setup - one time action, one can set up wallet for mainnet or testnet
  * wallet_recover - one time action, one can recover a wallet with a private key
* Properties
  * my_balance - provides info about wallet balance
  * my_funding_address - get info about wallet address in case you need to fund your wallet
  * payment_address - get payment address for new transaction. Funds received on the payment address are forwarded to your wallet. Payment address is displayed to entity paying for a service. 
  * private_key - get private key for backup
  * send_payment - send funds from your wallet to specified address in case you need to perform automatic payments to an entity
  * ticker - get info on the current value of DASH in USD. Useful for calculating the amount of DASH you need to receive for your service.
* Events
  * dash_payments - you should subscribe to this event to receive notifications each time someone sends you funds to unique payment address.
  
  
### Bitcoin micropayment service

Bitcoin micropayment service exposes the following:

* Actions
  * wallet_setup - one time action, one can set up wallet for mainnet or testnet
  * wallet_recover - one time action, one can recover a wallet with a private key
* Properties
  * my_balance - provides info about wallet balance
  * my_funding_address - get info about wallet address in case you need to fund your wallet
  * payment_address - get payment address for new transaction. Funds received on the payment address are forwarded to your wallet. Payment address is displayed to entity paying for a service. 
  * private_key - get private key for backup
  * send_payment - send funds from your wallet to specified address in case you need to perform automatic payments to an entity
  * ticker - get info on the current value of BITCOIN in USD. Useful for calculating the amount of BITCOIN you need to receive for your service.
* Events
  * bitcoin_payments - you should subscribe to this event to receive notifications each time someone sends you funds to unique payment address.

### Repository service

Repository service exposes the following:

* Actions
  * repository_setup - one time action of setting up a smart contract for data management
* Properties
  * create_asset - writes an asset described with a key, value pair  (both arbitrary strings) to the blockchain. Returns a transaction ID.  
  * read_asset_by_key - reads the asset from the blockchain. Returns the entire asset. 
  * update_asset - updates an asset’s value. Returns a transaction ID.
  * invalidate_asset - sets the asset’s state to deleted. While the assets on the blockchain cannot be deleted, their state can be removed from the “world state”. The asset is still on the ledger.
  * read_assets_by_key_range - when keys are supplied with a natural ordering (1..5, a...z, key1...key5, etc.), the function returns a list of assets whose keys are in the range that is supplied. 
  * read_asset_history - returns the entire transaction history tied to a particular blockchain asset (does not include queries).
  * couchdb_query_assets - allows to run complex couchDB queries. Returns a list of assets that satisfy the query supplied. 

# Adapter usage

A Vicinity user/device/service that wants to use services from the exposed BARTER adapter will communicate it's requests via the local agent to the remote agent (through the Vicinity ecosystem) running the BARTER adapter. APIs for using the BARTER adapter are documented in the provided [POSTMAN collection](https://drive.google.com/file/d/1rbcUwmbuuOjT5JqWP8r7nB8m4TurJvIR/view). Alongside, a [POSTMAN environment](https://drive.google.com/file/d/1jP3m08pxNYHN3ZXrGXYmpudKiGUr0rke/view) is also provided. 

# Validation 

BARTER is validated in smart parking ecosystem. There are two smart parking reservation scenarios covered within smart parking. 

The first one covers end user to platform/system parking reservation and payment. This scenario handles the situation when an end-user wants to reserve a smart parking spot at a smart garage, equipped with smart access automatic door unlocking. A working demonstration of this scenario can be viewed [here](https://www.youtube.com/watch?v=jrqIGyOWNDU). The web dashboard for parking space reservations can be accessed from [here](http://smartgarage.block-chain-labs.com:8000).

The second scenario covers autonomous platform to platform (M2M) parking reservation and payments. In this case direct, automated platform-to-platform parking reservation and payments are covered, without involving human users. A working demonstration of this scenario can be viewed [here](https://www.youtube.com/watch?v=CD2j8u2hmUs). The web dashboard for parking space reservations can be accessed from [here](http://smarthotel.block-chain-labs.com:8000).

