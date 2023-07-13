import hashlib

from .key import PrivateKey
from scripts.words import create_seed_phrase


class Wallet(object):
    __base = 'nivalty'

    def __init__(self, address: str) -> None:
        self.address = address
        self.balance = 0

        self.seed_phrase = None
        self.private_key = None

    def set_seed_phrase(self, seed_phrase: str) -> None:
        self.seed_phrase = seed_phrase
        self.private_key = PrivateKey(seed_phrase)

    @staticmethod
    def get_address_from_private_key(private_key: PrivateKey) -> str:
        _hash = hashlib.sha256()
        _hash.update(str(private_key).encode())
        return Wallet.__base + _hash.hexdigest()

    @staticmethod
    def create_new():
        seed_phrase = create_seed_phrase()
        private_key = PrivateKey(seed_phrase)
        address = Wallet.get_address_from_private_key(private_key)
        wallet = Wallet(address)
        wallet.set_seed_phrase(seed_phrase)
        return wallet
