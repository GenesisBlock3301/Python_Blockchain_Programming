from web3 import Web3

# node provide
node_provider = "https://mainnet.infura.io/v3/b2f38dd6fdef4888bb2b96c5aca98b62"

# create connection client to ethereum network.
web3_connection = Web3(Web3.HTTPProvider(node_provider))

# is connected or not
def are_we_connected():
    print(web3_connection.isConnected())

# find latest block
def latest_block():
    print(web3_connection.eth.block_number)

# balance of specific address of network.
def balancOf(ETH_address):
    balance = web3_connection.eth.get_balance(ETH_address)
    balance_ETH = web3_connection.fromWei(balance,'ether')
    print(balance_ETH)

balancOf("0xEA674fdDe714fd979de3EdF0F56AA9716B898ec8")
latest_block()
are_we_connected()
