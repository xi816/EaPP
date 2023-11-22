import kws

from pprint import pprint

from eapptypes import TokenType, Token
from eapplexfuns import *

def lex(prog):
    prog += "\0"

    buf = ["", ""]
    tokens = []
    pos = 0
    while (prog[pos] != "\0"):
        if (iscdig(prog[pos])):
            while (iscdig(prog[pos])):
                buf[0] += prog[pos]
                pos += 1
            tokens.append(Token(TYPE = TokenType.INTLIT, VALUE = buf[0]))
            buf[0] = ""
        elif (iswhite(prog[pos])):
            pos += 1
        else:
            while (not iswhite(prog[pos])):
                buf[1] += prog[pos]
                pos += 1
            if (buf[1] in kws.stdkws):
                tokens.append(Token(TYPE = TokenType.KEYWORD, VALUE = buf[1]))
            else:
                tokens.append(Token(TYPE = TokenType.IDENT, VALUE = buf[1]))
            buf[1] = ""

    return tokens

