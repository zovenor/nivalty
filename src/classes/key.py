import hashlib
from dataclasses import dataclass

from .types import SeedPhrase


@dataclass
class PrivateKey(object):
    seed_phrase: SeedPhrase

    def __post_init__(self):
        self.private_key = self.get_hash()

    def get_hash(self) -> str:
        _hash = hashlib.sha256()
        _hash.update(str(self.seed_phrase).encode())
        return _hash.hexdigest()
