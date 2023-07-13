import pickle

from classes.block import BlockChain

blockchain = BlockChain()
blockchain.load()

print(blockchain)
blockchain.save_blockchain(path)
