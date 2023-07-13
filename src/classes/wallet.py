import hashlib
from dataclasses import dataclass
from typing import List

from .key import PrivateKey
from .types import Address, SeedPhrase
from .token import Token
from src.scripts.words import create_seed_phrase
from src.settings import ADDRESS_PREFIX


@dataclass
class Wallet(object):
    address: Address

    balances: List[Token] = None
    private_key: PrivateKey = None

    __seed_phrase = None

    @property
    def seed_phrase(self) -> SeedPhrase:
        return self.seed_phrase

    @seed_phrase.setter
    def seed_phrase(self, seed_phrase: SeedPhrase) -> None:
        self.__seed_phrase = seed_phrase
        self.private_key = PrivateKey(seed_phrase)

    @staticmethod
    def get_address_from_private_key(private_key: PrivateKey) -> str:
        _hash = hashlib.sha256()
        _hash.update(str(private_key).encode())
        return ADDRESS_PREFIX + _hash.hexdigest()

    @staticmethod
    def create_new():
        seed_phrase = create_seed_phrase()
        private_key = PrivateKey(seed_phrase)
        address = Wallet.get_address_from_private_key(private_key)
        wallet = Wallet(address)
        wallet.seed_phrase = seed_phrase
        return wallet
