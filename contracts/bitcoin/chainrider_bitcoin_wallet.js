'use strict';
const shim = require('fabric-shim');
const util = require('util');
const got = require('got');
let log4js = require('log4js');
let logger = log4js.getLogger('ChaincodeLogger');
let bitcore = require('bitcore-lib');

let token = ''
let blockchain = ''
let privateKey = ''
let address = ''
let network = ''
let secret = ''
// Addresses
let ip_address_main = 'https://api.chainrider.io/v1/bitcoin/main'
let ip_address_testnet = 'https://api.chainrider.io/v1/bitcoin/testnet'
let base_url_ticker = 'https://api-dot-vizlorepaymentprocessor.appspot.com/v1/finance'
let base_url = ''

let Chaincode = class {
  // Init - is called every time upon instantiation and it can be used to set initial values of variables. 
  // In this case, the logger level is being set
  async Init(stub) {
    let ret = stub.getFunctionAndParameters();
    let args = ret.params;
    if (args.length != 2) {
      return shim.error('Incorrect number of arguments. Expecting 2.');
    }

    logger.level = 'info'
    token = 'o2IEP1p50pe1jfDtz8osOc7RpWZkwbfp'
    blockchain = args[0]
    secret = args[1]
    // private_key = NaN

    logger.info('blockchain %s', blockchain)

    //generating new private key
    // if (private_key == 'None')
    privateKey = new bitcore.PrivateKey('b221d9dbb083a7f33428d7c2a3c3199dec34a24d70210e28716ccaa7cd4ddb79');

    if ( !(blockchain == 'main' || blockchain == 'testnet') ){
      return shim.error('Unsupported blockchain network');
    }
    if (blockchain == 'main')
      base_url = ip_address_main
    else
      base_url = ip_address_testnet

    network = bitcore.Networks.livenet
    address = privateKey.toAddress(network);
    if(blockchain=='testnet'){
        network = bitcore.Networks.testnet
        address = privateKey.toAddress(network);
    }

    logger.info('=========== Instantiated Chaincode ===========');
    return shim.success();
  }

  // Invoke - neccessary for every chaincode (it invokes other chaincode methods)
  async Invoke(stub) {
    logger.info('Transaction ID: ' + stub.getTxID());
    logger.info(util.format('Args: %j', stub.getArgs()));

    let ret = stub.getFunctionAndParameters();
    logger.info(ret);
    try {
      let method = this[ret.fcn];
      if (!method) {
        logger.info('no function of name:' + ret.fcn + ' found');
        throw new Error('Received unknown function ' + ret.fcn + ' invocation');
      }
        logger.info(`=========== Invoking ${ret.fcn} ===========`);
        let payload = await method(stub, ret.params, this);
        logger.info('Payload is %s', JSON.stringify(payload))
        return shim.success(payload);
    } catch (err) {
      logger.info(err);
      return shim.error(err);
    }
  }
  
  async changeToken (stub, args, thisClass){
    if (args.length!=2){
      logger.info('Function must receive 2 parameters.');
      throw new Error('Function must receive 2 parameters.');
    }
    let oldToken = args[0]
    let newToken = args[1]
    if (oldToken === token){
      logger.info('Old and current tokens are the same -- continuing with the change.');
      token = newToken
    }
    logger.info('Token successfully changed from %s, to %s', oldToken, token)
    let res = {
      message: 'Token successfully changed'
    }
    return Buffer.from(JSON.stringify(res))  }

  // Get wallet private key 
  async getPrivateKey (stub, args, thisClass){
    if (args.length!=1){
      return Buffer.from('Function must receive 1 parameter.')
    }
    if (secret === args[0]){
      let res = {
        private_key: privateKey.toString()
      }
      return Buffer.from(JSON.stringify(res))
    }
    else{
      return Buffer.from('Invalid secret.')    
    }
  }

  // Get wallet funcing address
  async getFundingAddress (stub, args, thisClass){
    if (secret === args[0]){
      logger.info('address: %s', address.toString())
      let res = {
        address: address.toString()
      }
      return Buffer.from(JSON.stringify(res))
    }
    else{
      return Buffer.from('Invalid secret.')    
    }
  }

  // Get wallet balance
 // notx --	Integer -- Default 0; If set to 1 transaction list will be ommitted.
 async getBalance (stub, args, thisClass){
  return new Promise(async function (resolve, reject) {
    if (args.length>1){
      reject(Buffer.from('Function must receive 1 parameter.'))
    }
    if (secret === args[0]){
      if (args[1])
        notx= args[1]
      thisClass.getAddressByHash(1).then(balance => {
        resolve(balance)
      }).catch (error => {
        reject(Buffer.from(error.toString()))
      })    
    }
    else{
      reject(Buffer.from('Invalid secret.'))    
    }    
  })
}

  // Get address by hash
  // noTxList --	Integer -- Default 0; If set to 1 transaction list will be ommitted.
  async getAddressByHash (notx){
    return new Promise(async function (resolve, reject) {
    
      let url = `${base_url}/addr/${address}?noTxList=${notx}&token=${token}`

      logger.info('Fetching from: %s', url)
      got(url).then(response => {
        resolve(Buffer.from(response.body))
      }).catch(error => {
        logger.error(error) 
        reject(Buffer.from(error.toString()))
      })
    })
  }

  // Get unspent outputs for address
  async getUnspentOutputsForAddress (){
    return new Promise(async function (resolve, reject) {
        let url = `${base_url}/addr/${address.toString()}/utxo?token=${token}`
        logger.info('Fetching from: %s', url)
        got(url).then(response => {
            resolve(response.body)
        }).catch(error => {
            logger.error(error)
            reject(null)
        })
    })
   
  }

  // Send/Broadcast raw transaction
  async sendRawTx (rawtx){
    return new Promise(async function (resolve, reject) {
        let url = `${base_url}/tx/send`;
        logger.debug('rawtx: %s', rawtx)
        let body = {
          rawtx: rawtx,
          token: token
        }

        logger.debug('body: %s', JSON.stringify(body))
        let headers = {
          'Content-Type':'application/json',
          'Accept':'application/json',
        };
    
        logger.info('Posting to: %s', url)
        got(url, {
          headers: headers,
          body: JSON.stringify(body)
        }).then(response => {
            resolve(response.body)
        }).catch(error => {
            logger.error(error)
            reject(null)
        })
    })
  }

  // Pay  
  async pay (stub, args, thisClass){
    return new Promise(async function (resolve, reject) {
      if (secret === args[0]){
        let destination_address = args[1]
        let amount = parseInt(args[2])

        logger.debug('destination_address: %s', destination_address)
        logger.debug('amount: '+ amount)

        if (!bitcore.Address.isValid(destination_address, network)){
          reject(Buffer.from('Invalid address.'))
        }
        if (!amount > 0){
          reject(Buffer.from('Amount is 0 or less.'))
        }

        let utxos_raw = await thisClass.getUnspentOutputsForAddress()
        utxos_raw = JSON.parse(utxos_raw)

        logger.debug(JSON.stringify(utxos_raw))

        let utxos = []
        let total_amount = 0

        for (let i=0; i<utxos_raw.length; i++){
            let utxo_obj = {
                txId : utxos_raw[i].txid,
                outputIndex : utxos_raw[i].vout,
                address : utxos_raw[i].address,
                script : utxos_raw[i].scriptPubKey,
                satoshis : utxos_raw[i].satoshis
            };
            logger.debug(JSON.stringify(utxo_obj))
            utxos.push(utxo_obj)

            total_amount+=utxos_raw[i].satoshis
            if(total_amount >= amount+10000)
                break;
        }
        if (total_amount < amount+10000){
          reject(Buffer.from('Insufficient funds.'))
        }

        logger.debug(JSON.stringify(utxos))

        let transaction = new bitcore.Transaction()
        .from(utxos)
        .to(destination_address, amount)
        .fee(10000)
        .change(address.toString())
        .sign(privateKey)
        
        try{
          transaction.serialize();
          let res = await thisClass.sendRawTx(transaction.toString())
          logger.info(res)
          if(res != null){
            resolve(Buffer.from(res))
          }
        }
        catch(err){
          logger.error("ERR: " + err);
          reject(Buffer.from(err.toString()))
        }  
      }
      else{
        reject(Buffer.from('Invalid secret.'))
      }    
    })
  }

  async createPaymentForward (){
    return new Promise(async function (resolve, reject) {
      let body = {
        destination_address: address.toString(),
        token: token,
        callback_url: 'http://machine5.barter.block-chain-labs.com:8000/api/wallets/bitcoin/events/aeysafpomufreGIYTJKLgfwRFJHpmrfFpzoologijalisehfPMgs'
      }

      let url = ''
      if (blockchain == 'main'){
        url = `http://${ip_address_main}/paymentforward`
      }
      else{
        url = `http://${ip_address_testnet}/paymentforward`
      }

      let headers = {
        'Content-Type':'application/json',
        'Accept':'application/json',
      };

      logger.info('Posting to: %s', url)
      logger.info('Body: %s', JSON.stringify(body))

      got(url, {
        headers: headers,
        body: JSON.stringify(body)
      }).then(response => {
        resolve(Buffer.from(response.body))
      }).catch(error => {
        logger.error(error) 
        reject(Buffer.from(error.toString()))
      })
    })
  }

  async getPaymentAddress (stub, args, thisClass){
    return new Promise(async function (resolve, reject) {
      if (args.length>1){
        reject(Buffer.from('Function must receive 1 parameter.'))
      }
      if (secret === args[0]){
        thisClass.createPaymentForward().then(result => {
          resolve(result)
        }).catch (error => {
          reject(Buffer.from(error.toString()))
        })    
      }
      else{
        reject (Buffer.from('Invalid secret.'))
      }    
    })
  }

  async ticker(stub, args, thisClass){
    return new Promise(async function (resolve, reject) {
        let method = 'realtime'
        let pair = 'BTCUSD'
        let analytics = false
        let exchanges = ["Binance", "Bitfinex", "Bitstamp", "Coinbase", "Gemini", "HitBTC", "Huobi", "Kraken", "Kucoin", "Poloniex"]
        let seconds = 3600

        let body = {
            pair: pair,
            analytics: analytics,
            exchanges: exchanges,
            token: token,
            seconds: seconds
        };

        let url = `${base_url_ticker}/vwap/${method}/`;
        let headers = {
            'Content-Type':'application/json',
            'Accept':'application/json',
            'Chain-Rider': token
        };
        logger.info('Fetching from: %s', url);
        logger.info('Body: %s', JSON.stringify(body));
        got(url, {
            headers: headers,
            body: JSON.stringify(body)
        }).then(response => {
            resolve(Buffer.from(response.body));
        }).catch(error => {
            logger.error(error);
            reject(Buffer.from(error.toString()));
        })
    })
  }
};

shim.start(new Chaincode());