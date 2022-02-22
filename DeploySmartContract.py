import os
import json
from dotenv import load_dotenv
from web3 import Web3
load_dotenv()

node_provider = os.environ["NODE_PROVIDER_LOCAL"]
web3_connection = Web3(Web3.HTTPProvider(node_provider))

contract_abi = os.environ["CONTRACT_ABI"]
contract_bytecode = os.environ["CONTRACT_BYTECODE"]

# Is connected or not
def are_we_connected():
    print(web3_connection.isConnected())
are_we_connected()
glabal_gas = 4500000
global_gas_price = web3_connection.toWei(8,"gwei")

def get_nonce(ETH_address):
    # every contract has unique nonce
    return web3_connection.eth.get_transaction_count(ETH_address)

def deploy_contract(secret_number,amount_ETH,owner,signature):
    guess_number = web3_connection.eth.contract(abi=contract_abi,bytecode=contract_bytecode)
    transact_body = {
        "nonce":get_nonce(owner),
        "value":web3_connection.toWei(amount_ETH,"ether"),
        'gas':glabal_gas,
        'gasPrice':global_gas_price,
    }
    # deployment contract
    deployment = guess_number.constructor(secret_number).buildTransaction(transact_body)

    # sign transaction of contract
    sign_txn = web3_connection.eth.account.sign_transaction(deployment,signature)
    result = web3_connection.eth.send_raw_transaction(sign_txn.rawTransaction)
    return result

print(deploy_contract(1000,10,os.environ["ADDRESS_1"],os.environ["PRIVATE_KEY_1"]))
