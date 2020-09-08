import os
import pathlib as pl
    
def removeExtension(name = ''):
    x = len(name) - 1
    dot = x
    found = False
    while( x > 0 and not found):
        if(name[x] == '.'):
            dot = x
            found = True

        x -= 1
    if(found):
        return name[:dot]
    else:
        return name


def cleanList(progs):
    for x in progs:
        if x[0] == '.' or pl.Path(x).is_dir():
            progs.remove(x)

def parseEcmsFolder():
    progs = os.listdir()

    cleanList(progs)
    
    for i,x in enumerate(progs):
        if(hasExtension(x)):
            progs[i] = removeExtension(x)
    return progs


def hasExtension(name = ''):
    x = len(name) - 1
    while( x > 0):
        if(name[x] == '.'):
            return True

        x -= 1
    return False