from typing import List, Dict
import time

from .wallet import Wallet
from .key import PrivateKey
from .token import Token


class Transaction(object):
    def __init__(self):
        self.type = None
        self.data = None
        self.private_key = None

    def create_account(self, name: str, private_key: PrivateKey):
        self.type = 'create_account'
        self.data = {
            "name": name,
            "address": Wallet.get_address_from_private_key(private_key),
            "timestamp": int(time.time())
        }
        self.private_key = private_key

    def send_tokens(self, sender: str, recipient: str, tokens: List[List]) -> None:
        self.type = 'send_tokens'
        self.data = {
            "sender": sender,
            "recipient": recipient,
            "tokens": tokens,
            "timestamp": int(time.time())
        }

    def from_dict(self, tp: str, d: Dict):
        self.type = tp
        self.data = d
