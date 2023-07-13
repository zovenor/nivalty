import json
import random

from src.settings import WORDS_PATH

with open(WORDS_PATH, 'r') as file:
    words = json.load(file)


def create_seed_phrase() -> str:
    __len = 16
    return ' '.join(words[random.Random().randint(a=0, b=len(words))] for _ in range(__len))
