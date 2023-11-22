def iscdig(c):
    return (len(c) == 1 and (c in "012345789"))

def isusdig(s):
    return (len(s) > 0 and (all([iscdig(c) for c in s])))

def isisdig(s):
    return (len(s) > 0 and ((isusdig(s)) or (s[0] == "-" and isusdig(s[1:]))))

def iswhite(c):
    return (c in " \t\n\b\v\0")

