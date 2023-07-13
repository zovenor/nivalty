from typing import Dict
import hashlib
from dataclasses import dataclass

from .types import Address
from src.settings import ADDRESS_PREFIX


@dataclass
class Token(object):
    symbol: str
    decimals: int
    name: str
    owner: Address

    def __post_init__(self):
        self.address = self.get_hash()

    def get_hash(self) -> str:
        _hash = hashlib.sha256()
        _hash.update(str(self.symbol).encode())
        _hash.update(str(self.decimals).encode())
        _hash.update(str(self.name).encode())
        _hash.update(str(self.owner).encode())
        return ADDRESS_PREFIX + _hash.hexdigest()
