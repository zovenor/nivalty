import time
from typing import List
import pickle
import json
import hashlib

from .token import Token
from .transaction import Transaction

import settings


class Block(object):
    def __init__(self, timestamp: float, data: List[Transaction], prev_hash: str, last_index: int) -> None:
        self.block_id = last_index + 1
        self.timestamp = int(timestamp)
        self.data = data
        self.prev_hash = prev_hash
        self.hash = self.get_hash()

    def get_hash(self) -> str:
        _hash = hashlib.sha256()
        _hash.update(str(self.block_id).encode('utf8'))
        _hash.update(str(self.timestamp).encode('utf8'))
        _hash.update(str(self.data).encode('utf8'))
        _hash.update(str(self.prev_hash).encode('utf8'))
        return _hash.hexdigest()


class BlockChain(object):
    def __init__(self):
        self.chain = []
        self.load()
        if not self.chain:
            first_block = Block(
                timestamp=time.time(),
                data=[],
                prev_hash='0',
                last_index=-1
            )
            self.add_block(first_block)
            self.__save_blockchain()

    def get_last_block(self) -> Block:
        return self.chain[-1]

    def add_block(self, block: Block) -> None:
        self.chain.append(block)

    def __save_blockchain(self, path: str = settings.CHAIN_PATH) -> None:
        with open(path, 'wb') as file:
            pickle.dump(self.chain, file)

    def load(self, path=settings.CHAIN_PATH):
        try:
            with open(path, 'rb') as file:
                self.chain = pickle.load(file)
        except FileNotFoundError:
            ...

    def send_tx(self, tx: Transaction) -> None:
        last_block = self.get_last_block()
        block = Block(
            timestamp=time.time(),
            data=[tx],
            prev_hash=last_block.hash,
            last_index=last_block.block_id
        )
        self.add_block(block)
        self.__save_blockchain()

    def get_balance(self, address) -> List[Token]:
        ...

    def __repr__(self):
        return json.dumps(
            [
                {
                    "block_id": block.block_id,
                    "timestamp": block.timestamp,
                    "data": [{
                        'type': tx.type,
                        'tx': tx.data
                    } for tx in block.data],
                    "prev_block": block.prev_hash,
                    "hash": block.hash
                }
                for block in self.chain
            ]
        )
