from classes.transaction import Transaction
from classes.token import Token
from classes.block import BlockChain

blockchain = BlockChain()


def create_new_token():
    token = Token(
        symbol='nivalty',
        decimals=18,
        owner='nivaltyaf61bad5171ee54718b22fb80a5d0c052b7ba26344ab773bee020262117a192c',
        name='Nivalty token'
    )
    tx = Transaction()
    tx.from_dict('create_new_token', {
        'symbol': token.to_dict()
    })
    blockchain.send_tx(tx)


def get_blockchain():
    print(blockchain)

# get_blockchain()
# create_new_token()