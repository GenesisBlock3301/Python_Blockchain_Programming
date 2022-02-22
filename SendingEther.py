import os
from web3 import Web3
from dotenv import load_dotenv
import json
load_dotenv()

node_provider = os.environ['NODE_PROVIDER_LOCAL']
web3_connection = Web3(Web3.HTTPProvider(node_provider))
glabal_gas = 4500000
global_gas_price = web3_connection.toWei(8,"gwei")

def get_nonce(ETH_address):
    return web3_connection.eth.get_block_transaction_count(ETH_address)

# Is connected or not
def are_we_connected():
    print(web3_connection.isConnected())

def transferETH(sender,receiver,signature,amount_ETH):
    transaction_body = {
        'nonce':0,
        'to':receiver,
        'value':web3_connection.toWei(amount_ETH,'ether'),
        'gas':glabal_gas,
        'gasPrice':global_gas_price,
    }
    # Sign transaction
    sign_transaction = web3_connection.eth.account.sign_transaction(transaction_body,signature)
    result = web3_connection.eth.send_raw_transaction(sign_transaction.rawTransaction)
    return result

print(transferETH(os.environ["ADDRESS_2"],os.environ["ADDRESS_1"],os.environ["PRIVATE_KEY_2"],2))