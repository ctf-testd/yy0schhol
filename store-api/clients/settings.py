"""
This module contains additional settings for clients app
"""
from enum import Enum
from typing import List, Tuple


class ClientsStatuses(Enum):
    DEFAULT = 'default'
    PREMIUM = 'premium'

    @classmethod
    def choices(cls) -> List[Tuple[str, str]]:
        return [(choice.value, choice.name) for choice in cls]



