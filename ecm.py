import os
import sys
import pathlib as pl
import subprocess

cmdList = []
cmdWithExtensions = []



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

def createGenericFile():
    pass

def cleanList(progs):
    for x in progs:
        if x[0] == '.' or pl.Path(x).is_dir():
            progs.remove(x)

def parseEcmsFolder():
    progs = os.listdir()
    print(progs)
    cleanList(progs)
    print(progs)
    
    for i,x in enumerate(progs):
        if(hasExtension(x)):
            progs[i] = removeExtension(x)
    return progs
    
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

def hasExtension(name = ''):
    x = len(name) - 1
    while( x > 0):
        if(name[x] == '.'):
            return True

        x -= 1
    return False

def hasProgram(name):
    if name in cmdList:
        return True
    return False

def main():

    SetupFiles() # Checks necessary if ecms exists
    os.chdir('./ecms')
    print('Hello! Type help to discover more commands.')

    """
    Main program Loop
    This loop handles the user input
    and redirects to the correponding script to be run
    """
    
    while(1):

        cmd = input( os.getcwd() + ":$ ") # Holds the user input
        
        if(cmd == "exit" or cmd == "q"):
            print('Bye!')
            break
        elif cmd == 'ul':
            global cmdList
            global cmdWithExtensions
            cmdList = parseEcmsFolder()
            cmdWithExtensions = os.listdir()
            print('List of Scripts updated.')
        else:
            if(hasProgram(cmd)):
                subprocess.run(['python3', cmd])
            else:
                print('There is no Script with that name.')

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt: # This is to not generate an error when you ctrl+c the program
        print()


print(cmdList)
"""

ADD NEW SCRIPT
REMOVE SCRIPT
CHECK SCRIPTS
CREATE FOLDER
CREATE EXAMPLE SCRIPT

"""        
