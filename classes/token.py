from typing import Dict
import hashlib


class Token(object):
    def __init__(self, symbol: str, decimals: int, name: str, owner: str):
        self.symbol = symbol
        self.decimals = decimals
        self.name = name
        self.owner = owner
        self.address = self.get_hash()

    def get_hash(self) -> str:
        _hash = hashlib.sha256()
        _hash.update(str(self.symbol).encode())
        _hash.update(str(self.decimals).encode())
        _hash.update(str(self.name).encode())
        _hash.update(str(self.owner).encode())
        return 'nivalty' + _hash.hexdigest()

    def to_dict(self) -> Dict:
        return {
            "symbol": self.symbol,
            "decimals": self.decimals,
            "name": self.name,
            "owner": self.owner,
            "address": self.address
        }
