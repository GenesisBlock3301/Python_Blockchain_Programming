# Python Blockchain Programming

# JSON RPC:

```JSON RPC is a protocol which is allows dapps to interact ethereum network.
Web3.py allow us to interact with network and this is possible only for JSON RPC.
```

# ABI
```
Application Binary Interface
This is a type of object that represent all functions that the contract has coded.
```

# Web3 transaction
```
SenderNonce --> ReceiverPublicAddress --> Amount --> TransactionFee --> SenderSignature.
```

# Add brownie network
```
brownie networks add {network_class} {your_network_name} host={your_host} chainid={your_chaid}

brownie console --network ganache-local

brownie networks delete ganache-local

brownie run scripts/deploy.py --network ganache-local
```