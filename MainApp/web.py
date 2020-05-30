import os
os.environ['WEB3_INFURA_PROJECT_ID'] = "640c09023e9944aebfd68341969fe6d6"
from web3 import Web3
from web3 import eth

infura_url = "https://ropsten.infura.io/v3/640c09023e9944aebfd68341969fe6d6"
web3 = Web3(Web3.HTTPProvider(infura_url))

ABI = [{"inputs": [{"internalType": "address payable", "name": "recipient", "type": "address"}], "name": "send",
        "outputs": [], "stateMutability": "payable", "type": "function"}]

contract = web3.eth.contract(address="0xeEF339ecB6c9E6f9d22ba1AE80FE9c8B3C0ae252", abi=ABI)

main_wallet = "0x37aF4b6d5Eb749168ce1d2Bce867725c292D6777"

homie ="0x5824Eb3377478571dcB83072dCA6Ca1973eF17EE"
def send(from_wallet, to_wallet, value):
    web3.eth.account = from_wallet
    contract_send = contract.functions.send(to_wallet).buildTransaction({
        'chainId': 3,
        'gas': 300000,
        'gasPrice': web3.eth.gasPrice,
        'nonce': web3.eth.getTransactionCount(from_wallet),
        'value': value,
    })
    key = '4ea5c6a03af8f674c4cdaf32fa50e7ffc94adbdbb0995924c8373f1817d08715'
    acct = eth.Account.privateKeyToAccount(key)
    tmp_txn = eth.Account.sign_transaction(contract_send, key)
    web3.eth.sendRawTransaction(tmp_txn.rawTransaction)


send(main_wallet, "0x5824Eb3377478571dcB83072dCA6Ca1973eF17EE", 10**18)
