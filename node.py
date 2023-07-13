from fastapi import FastAPI
from src.classes.block import BlockChain
import json

app = FastAPI()
blockchain = BlockChain()


@app.get('/')
def get_last_block():
    return blockchain.get_last_block()
