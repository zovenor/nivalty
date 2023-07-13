import hashlib


class PrivateKey(object):
    def __init__(self, seed_phrase: str):
        self.seed_phrase = seed_phrase
        self.private_key = self.get_private_key()

    def get_private_key(self):
        _hash = hashlib.sha256()
        _hash.update(str(self.seed_phrase).encode())
        return _hash.hexdigest()

    def __repr__(self) -> str:
        return self.private_key
