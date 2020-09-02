import os
import pathlib as pl

def hasScriptFolder():
    path = pl.Path('ecms')
    if path.exists() and path.is_dir():
        return True
    else:
        return False

def ScriptFolder():

    if not hasScriptFolder():
        try:
            os.mkdir('ecms')
        except Exception:
            print('Could Not Create Script Folder.')
            exit(1)
    return

def SetupFiles():
    if not hasScriptFolder():
        print('It seems this is the first time you run this program or is making a reinstallation.')
        ans = input('Would you like me to create the startup files? [y/n]: ')
        if ans == 'y':

            print('Creating script folder....')
            ScriptFolder()
            print('Script folder Created at ' + str(pl.Path('ecms')) + '.')