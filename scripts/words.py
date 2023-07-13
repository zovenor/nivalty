import json
import random

from settings import DATADIR_PATH

path = DATADIR_PATH + '/words.json'

with open(path, 'rb') as file:
    words = json.load(file)


def create_seed_phrase() -> str:
    __len = 16
    return ' '.join(words[random.Random().randint(a=0, b=len(words))] for _ in range(__len))
