from typing import NewType, Union

Address = Union[NewType('Address', str), str]
Hash = Union[NewType('Hash', str), str]
SeedPhrase = Union[NewType('SeedPhrase', str), str]
