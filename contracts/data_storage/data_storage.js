'use strict';
const shim = require('fabric-shim');
const util = require('util');
var log4js = require('log4js');
var logger = log4js.getLogger('ChaincodeLogger');

let secret = ''

let Chaincode = class {

  // ===============================================
  // Init - is called every time upon instantiation and it can be used to set initial values of variables. 
  // In this case, the logger level is being set. 
  // ===============================================
  async Init(stub) {
    let ret = stub.getFunctionAndParameters();
    let args = ret.params;
    if (args.length != 1) {
      return shim.error('Incorrect number of arguments. Expecting 1.');
    }
    logger.level = 'info'
    secret = args[0]
    logger.info('=========== Instantiated Chaincode ===========');
    return shim.success();
  }

  // ===============================================
  // Invoke - neccessary for every chaincode (it invokes other chaincode methods)
  // ===============================================
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
      return shim.success(payload);
    } catch (err) {
      logger.info(err);
      return shim.error(err);
    }
  }

  // ===============================================
  // create - writes an asset to the ledger, where asset is represented as: (key, value)
  // ===============================================
  async create(stub, args, thisClass) {
    if (args.length != 3) { 
			throw new Error('Incorrect number of arguments. Expecting 3.');
    }
    
    if (secret !== args[0]){
      throw new Error('Invalid secret.');
    }

    let key = args[1]; 
    let value = args[2];

    let assetState = await stub.getState(key);
    if (assetState.toString()) {
        throw new Error('This asset already exists: ' + key);
    }

    if (key.length <= 0) { 
        throw new Error('Argument [1] key must be a non-empty string'); 
    }
    if (value.length <= 0) { 
        throw new Error('Argument [2] value must be a non-empty string'); 
    }

    let asset = {};
    asset.key = key;
    asset.value = value;

    await stub.putState(key, Buffer.from(JSON.stringify(asset)));
  }

  // ===============================================
  // read - reads an asset from state by key
  // ===============================================
  async read(stub, args, thisClass) {
    if (args.length != 2) {
      throw new Error('Incorrect number of arguments. Expecting 2.');
    }

    if (secret !== args[0]){
      throw new Error('Invalid secret.');
    }

    let key = args[1];
    if (!key) {
      throw new Error(' Asset key must not be empty');
    }

    let assetAsBytes = await stub.getState(key);
    if (!assetAsBytes.toString()) {
      let jsonResp = {};
      jsonResp.Error = 'Asset does not exist: ' + key;
      throw new Error(JSON.stringify(jsonResp));
    }

    logger.info('=======================================');
    logger.info(assetAsBytes.toString());
    logger.info('=======================================');

    return assetAsBytes;
  }

  // ==================================================
  // delete - as there is no delete on the blockchain, delete function marks the asset as deleted. 
  // The asset will no longer be searchable by key, but it's entire history remains on the ledger. 
  // ==================================================
  async delete(stub, args, thisClass) {

    if (args.length != 2) {
      throw new Error('Incorrect number of arguments. Expecting 2.');
    }
    if (secret !== args[0]){
      throw new Error('Invalid secret.');
    }

    let keyName = args[1];
    if (!keyName) {
      throw new Error('key name must not be empty');
    }

    let valAsbytes = await stub.getState(keyName); 
    let jsonResp = {};
    if (!valAsbytes) {
      jsonResp.error = 'key does not exist: ' + name;
      throw new Error(jsonResp);
    }
    let asset = {};
    try {
      asset = JSON.parse(valAsbytes.toString());
    } catch (err) {
      jsonResp = {};
      jsonResp.error = 'Failed to decode JSON of: ' + keyName;
      throw new Error(jsonResp);
    }
    await stub.deleteState(keyName); 
  }

  // ===========================================================
  // update - updates the asset value for a given asset key
  // ===========================================================
  async update(stub, args, thisClass) {
		if (args.length != 3) {
			throw new Error('Incorrect number of arguments. Expecting 3.')
    }
    if (secret !== args[0]){
      throw new Error('Invalid secret.');
    }

		let key = args[1];
		let newValue = args[2];
		logger.info('- Start updating asset - ');
		let assetAsBytes = await stub.getState(key);
		if (!assetAsBytes || !assetAsBytes.toString()) {
			throw new Error('Asset does not exist');
		}
		var asset = {};
		try {
			asset = JSON.parse(assetAsBytes.toString());
		} catch (err) {
			let jsonResp = {};
			jsonResp.error = 'Failed to decode JSON of: ' + key;
			throw new Error(jsonResp);
		}
		logger.info(asset);
		asset.value = newValue;
		let assetJSONasBytes = Buffer.from(JSON.stringify(asset));
		await stub.putState(key, assetJSONasBytes);
    logger.info(asset);
    }

    // ===========================================================================================
    // Read Assets By Key Range - performs a range query based on the start and end keys provided.
    // ===========================================================================================
    async getAssetByKeyRange(stub, args, thisClass) {
      if (args.length != 3) {
          throw new Error('Incorrect number of arguments. Expecting 3.')
      }

      if (secret !== args[0]){
        throw new Error('Invalid secret.');
      }
  

      let startKey = args[1]
      let endKey = args[2]

      let resultsIterator = await stub.getStateByRange(startKey, endKey)
      let method = thisClass['getAllResults']
      let results = await method(resultsIterator, false)

      return Buffer.from(JSON.stringify(results))
  }

  // ===============================================
  // getHistoryForAsset - gets all previous transactions for asset
  // ===============================================
  async getHistoryForAsset(stub, args, thisClass) {
      if (args.length != 2) {
      throw new Error('Incorrect number of arguments. Expecting 2.')
      }

      if (secret !== args[0]){
        throw new Error('Invalid secret.');
      }
 
      let key = args[1]
      console.info('- start getHistoryForAsset: %s', key)
  
      let resultsIterator = await stub.getHistoryForKey(key)
      let method = thisClass['getAllResults']
      let results = await method(resultsIterator, true)
  
      return Buffer.from(JSON.stringify(results))
  }
  
  // ===============================================
  //  Ad hoc rich query
  // ===============================================
  async queryAssets(stub, args, thisClass) {
      if (args.length != 2) {
          throw new Error('Incorrect number of arguments. Expecting 2.')
      }

      if (secret !== args[0]){
        throw new Error('Invalid secret.');
      }

      let queryString = args[1]
      if (!queryString) {
          throw new Error('queryString must not be empty')
      }
      let method = thisClass['getQueryResultForQueryString']
      let queryResults = await method(stub, queryString, thisClass)
      return queryResults
  }

  // ===============================================
  // getAllResults - packs the results to JSON array
  // ===============================================
  async getAllResults(iterator, isHistory) {
      let allResults = []
      while (true) {
      let res = await iterator.next()

      if (res.value && res.value.value.toString()) {
          let jsonRes = {}
          console.log(res.value.value.toString('utf8'))
          if (isHistory && isHistory === true) {
              jsonRes.TxId = res.value.tx_id
              jsonRes.Timestamp = res.value.timestamp
              jsonRes.IsDelete = res.value.is_delete.toString()
              try {
                  jsonRes.Value = JSON.parse(res.value.value.toString('utf8'))
              } catch (err) {
                  console.log(err)
                  jsonRes.Value = res.value.value.toString('utf8')
              }
          } else {
              jsonRes.Key = res.value.key
              try {
                  jsonRes.Record = JSON.parse(res.value.value.toString('utf8'))
              } catch (err) {
                  console.log(err)
                  jsonRes.Record = res.value.value.toString('utf8')
              }
          }
          allResults.push(jsonRes)
      }
      if (res.done) {
          console.log('end of data')
          await iterator.close()
          console.info(allResults)
          return allResults
          }
      }
  }

  // =========================================================================================
  // getQueryResultForQueryString executes the passed in query string.
  // Result set is built and returned as a byte array containing the JSON results.
  // =========================================================================================
  async getQueryResultForQueryString(stub, queryString, thisClass) {
      console.info('- getQueryResultForQueryString queryString:' + queryString)
      let resultsIterator = await stub.getQueryResult(queryString)
      let method = thisClass['getAllResults']
      let results = await method(resultsIterator, false)
      return Buffer.from(JSON.stringify(results))
  }
};

shim.start(new Chaincode());
