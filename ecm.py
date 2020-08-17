import os
import sys
import pathlib as pl
from shutil import rmtree
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
        ScriptFolder()
        createHelpFile()


def createHelpFile():
    f = open('ecms/help.py', 'w')
    f.write(
"""
import os

def main():
    print('This is all of the available scripts.')
    print('Type the name of the file and any necessary arguments.')
    p = os.listdir()
    for file in p:
        print(file)


if __name__ == "__main__":
    main()
""")
    f.flush()
    f.close()

def createExampleFile():
    pass

def createGenericFile():
    pass

def main():
    rmtree('ecms')
    SetupFiles() # Checks necessary if ecms exists
    print('Hello! Type help to discover more commands.')

    """
    Main program Loop
    This loop handles the user input
    and redirects to the correponding script to be run
    """
    while(1):

        cmd = input("$ ") # Holds the user input
        
        if(cmd == "exit" or cmd == "q"):
            print('Bye!')
            break
        else:
            print('hey')


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt: # This is to not generate an error when you ctrl+c the program
        print()



"""

ADD NEW SCRIPT
REMOVE SCRIPT
CHECK SCRIPTS
CREATE FOLDER
CREATE EXAMPLE SCRIPT

"""        
