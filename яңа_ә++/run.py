import lexeapp
import parseeapp

from sys import argv
from os import system
from os.path import dirname

CFILE = dirname(__file__)

try:
    inputFile = argv[1]
except Exception:
    raise TypeError("No input file provided!")

try:
    autoCompile = argv[2] == "-a"
except Exception:
    autoCompile = False

outputFile = ".".join(inputFile.split(".")[:-1])

with open(inputFile, "r") as fl:
    src = fl.read()
toks = lexeapp.lex(src)
with open(outputFile + ".asm", "w") as fl:
    fl.write(parseeapp.parseToks(toks, f"{CFILE}/puti.asm.snp"))
if (autoCompile):
    system(f"nasm -f elf64 \"{CFILE}/{outputFile + '.asm'}\" -o \"{CFILE}/{outputFile + '.o'}\"")
    system(f"ld \"{CFILE}/{outputFile + '.o'}\" -o \"{CFILE}/{outputFile}\"")

