import dataclasses
import time
from typing import List
import hashlib
from dataclasses import dataclass
import json

from .types import Hash
from .transaction import Transaction
from src.settings import CHAIN_PATH


@dataclass
class Block(object):
    block_id: int
    prev_hash: Hash
    data: List[Transaction]
    timestamp: int

    def __post_init__(self):
        self.block_id += 1
        self.timestamp = int(self.timestamp)
        self.current_hash = self.get_hash()

    def get_hash(self) -> str:
        _hash = hashlib.sha256()
        _hash.update(str(self.block_id).encode('utf8'))
        _hash.update(str(self.timestamp).encode('utf8'))
        _hash.update(str(self.data).encode('utf8'))
        _hash.update(str(self.prev_hash).encode('utf8'))
        return _hash.hexdigest()


@dataclass
class BlockChain(object):
    chain: List[Block] = None

    def __post_init__(self):
        self.load()
        if not self.chain:
            first_block = Block(
                timestamp=int(time.time()),
                data=[],
                prev_hash='0',
                block_id=-1,
            )
            self.add_block(first_block)
            self.__save_blockchain()

    def get_last_block(self) -> Block:
        return self.chain[-1]

    def add_block(self, block: Block) -> None:
        self.chain.append(block)

    def __save_blockchain(self, path: str = CHAIN_PATH) -> None:
        with open(path, 'w') as file:
            json.dump([dataclasses.asdict(block) for block in self.chain], file)

    def load(self, path=CHAIN_PATH):
        try:
            with open(path, 'r') as file:
                self.chain = json.load(file)
        except FileNotFoundError:
            ...
        except json.decoder.JSONDecodeError:
            ...

    # def send_tx(self, tx: Transaction) -> None:
    #     last_block = self.get_last_block()
    #     block = Block(
    #         timestamp=time.time(),
    #         data=[tx],
    #         prev_hash=last_block.hash,
    #         last_index=last_block.block_id
    #     )
    #     self.add_block(block)
    #     self.__save_blockchain()
    #
    # def get_balance(self, address) -> List[Token]:
    #     ...
    #
    # def __repr__(self):
    #     return json.dumps(
    #         [
    #             {
    #                 "block_id": block.block_id,
    #                 "timestamp": block.timestamp,
    #                 "data": [{
    #                     'type': tx.type,
    #                     'tx': tx.data
    #                 } for tx in block.data],
    #                 "prev_block": block.prev_hash,
    #                 "hash": block.hash
    #             }
    #             for block in self.chain
    #         ]
    #     )
