import os
import json
from dotenv import load_dotenv
from web3 import Web3
load_dotenv()

node_provider = os.environ["NODE_PROVIDER_LOCAL"]
web3_connection = Web3(Web3.HTTPProvider(node_provider))

contract_abi = json.loads(os.environ["CONTRACT_ABI"])
contract_address = os.environ["ADDRESS_1"]
contract_bytecode = os.environ["CONTRACT_BYTECODE"]

glabal_gas = 4500000
global_gas_price = web3_connection.toWei(8,"gwei")

def get_nonce(ETH_address):
    # every contract has unique nonce
    return web3_connection.eth.get_transaction_count(ETH_address)

# Is connected or not
def are_we_connected():
    print(web3_connection.isConnected())

def get_balance():
    contract = web3_connection.eth.contract(address=os.environ["CONTRACT_CREATE_ADDRESS"],abi=contract_abi)
    balance_contract = web3_connection.fromWei(contract.functions.getBalance().call(),"ether")
    return balance_contract

def play(player,guess,amount_ETH,signature):
    contract = web3_connection.eth.contract(address=os.environ["CONTRACT_CREATE_ADDRESS"],abi=contract_abi)
    transact_body = {
        "nonce":get_nonce(player),
        "value":web3_connection.toWei(amount_ETH,"ether"),
        'gas':glabal_gas,
        'gasPrice':global_gas_price,
    }
    transaction = contract.functions.play(player,guess).buildTransaction(transact_body)
    sing_tnx = web3_connection.eth.sign_transaction(transaction,signature)
    result = web3_connection.eth.send_raw_transaction(sing_tnx.rawTransaction)
    return result

# print(get_balance())
print(play(os.environ["ADDRESS_2"],1000,1,os.environ["PRIVATE_KEY_2"]))
