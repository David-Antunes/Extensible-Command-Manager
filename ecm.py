import os
import sys
import pathlib as pl
import subprocess

# Importing local Files
import file_creation
import file_parser
import setup_files

cmdList = []
cmdWithExtensions = []
path = []
colors = []
execute_file = {}

def hasProgram(name):
    if name in cmdList:
        return True
    return False

def main():

    setup_files.SetupFiles() # Checks necessary if ecms exists
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
        else:
            
            global cmdList
            global cmdWithExtensions

            cmdList = file_parser.parseEcmsFolder()
            
            cmdWithExtensions = os.listdir()

            if(hasProgram(cmd)):
                subprocess.run(['python3', cmdWithExtensions[cmdList.index(cmd)]])
            else:
                print('There is no Script with that name.')

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
