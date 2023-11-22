from enum import Enum, auto
from dataclasses import dataclass

class TokenType(Enum):
    INTLIT = auto()
    KEYWORD = auto()
    IDENT = auto()

@dataclass
class Token:
    TYPE: str
    VALUE: str

