from classes.block import BlockChain
from classes.wallet import Wallet
from classes.transaction import Transaction
from pprint import pprint

wallet = Wallet.create_new()
tx = Transaction()
tx.create_account('zovenor', wallet.address)

blockchain = BlockChain()
pprint(blockchain)
# blockchain.send_tx(tx)
