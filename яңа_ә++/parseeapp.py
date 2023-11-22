from dataclasses import dataclass
from eapptypes import TokenType, Token

def rfl(fln):
    with open(fln, "r") as fl:
        return fl.read()

@dataclass
class TypeElem:
    TP: str
    VAL: str

def parseToks(toks, *asmSnippets):
    out = "section .text\n"
    for snip in asmSnippets:
        out += rfl(snip) + "\n"
    out += "global _start\n_start:\n"
    pos = 0
    tpc = []
    chars = []

    while (True):
        ct = toks[pos]
        if (ct.TYPE == TokenType.INTLIT):
            out += f"  mov rax, {ct.VALUE}\n"
            out += f"  push rax\n"
            tpc.append(TypeElem("int", ct.VALUE))
        elif (ct.TYPE == TokenType.KEYWORD):
            if (ct.VALUE == "+"):
                assert len(tpc) >= 2, f"Expected 2 arguments for `+`, but found {len(tpc)}."
                assert tpc[-2].TP == "int", f"Arguments of `+` are {int, int}, but found {tpc[-2].TP} in the stack in position {len(tpc)-2}."
                assert tpc[-1].TP == "int", f"Arguments of `+` are {int, int}, but found {tpc[-1].TP} in the stack in position {len(tpc)-1}."
                tpc.pop()
                out += f"  pop rax\n"
                out += f"  pop rbx\n"
                out += f"  add rax, rbx\n"
                out += f"  push rax\n"
            elif (ct.VALUE == "<-санны-яз!"):
                assert len(tpc) >= 1, f"Expected 1 argument for `<-санны-яз!`, but found {len(tpc)}."
                assert tpc[-1].TP == "int", f"Arguments of `<-санны-яз!` are {int}, but found {tpc[-1].TP} in the stack in position {len(tpc-1)}."
                tpc.pop()
                out += f"  pop rdi\n"
                out += f"  call puti\n"
            elif (ct.VALUE == "<-хәрефне-яз!"):
                assert len(tpc) >= 1, f"Expected 1 argument for `<-хәрефне-яз!`, but found {len(tpc)}."
                assert tpc[-1].TP == "int", f"Arguments of `<-хәрефне-яз!` are {int}, but found {tpc[-1].TP} in the stack in position {len(tpc-1)}."
                out += f"  mov rax, 1\n"
                out += f"  mov rdi, 1\n"
                if (int(tpc[-1].VAL) in chars):
                    out += f"  mov rsi, c{chars.index(int(tpc[-1].VAL))}\n"
                else:
                    chars.append(int(tpc[-1].VAL))
                    out += f"  mov rsi, c{chars.index(int(tpc[-1].VAL))}\n"
                out += f"  mov rdx, 1\n"
                out += f"  syscall\n"
                tpc.pop()
            elif (ct.VALUE == "бетте!"):
                out += f"  mov rax, 60\n"
                out += f"  pop rdi\n"
                out += f"  syscall\n"
        pos += 1

        if (pos == len(toks)):
            break
    out += f"segment .data:\n"
    for i, j in enumerate(chars):
        out += f"c{i}: db {j}\n"
    return out

