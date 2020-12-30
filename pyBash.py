import os
import sys
import pathlib as pl
import subprocess
from colorama  import Fore,Back,Style, init, deinit

DEBUG = True

# Displays the prompt in the pyBash
prompt = ''
# Displays the symbol of line in pyBash
prompt_symbol = ''
# Directories to verify if there is a corresponding script to be executed
path = []

# Structure of colors inside the pyBash
colors = {}

# Extensions the program recognizes and will try to execute
execute_file = {}


# initial values
# delete after config files are done

prompt = os.getcwd()
prompt_symbol = ':$ '
colors = {
    'prompt' : Fore.GREEN,
    'prompt_symbol' : Fore.BLUE,
}
path = [os.getcwd() + '/ecms',]
execute_file = {
    '.py' : 'python3',
}

def execute_script(cmd='',args=[]):
    if(cmd == ''):
        print()
    else:
        extension = get_file_extension(cmd)
        prog_to_exec = cmd + extension

        if extension in execute_file:

            subprocess.run([execute_file.get(extension), get_file_path(prog_to_exec) + ''.join(args)])
        else:
            print('No script with that name.')

def get_file_extension(cmd=''):

    for ph in path:
        prog_list = os.listdir(ph)
        for prog in prog_list:
            prog = prog.split('.')
            
            if prog[0] == cmd:
                return ('.' + prog[-1])
        
    return ''

def get_file_path(filename):
    if filename == '':
        return ''
    
    for ph in path:
        prog_list = os.listdir(ph)
        for prog in prog_list:
            if prog == filename:
                return os.path.realpath(ph + '/' + filename)


def change_dir(cmd = []):

    if len(cmd) == 0:
        print('cd [Directory name] or [absolute Path ex: /home/example]')
        return 0
    
    global prompt
    if(os.path.isdir(cmd[0])):
        os.chdir(cmd[0])
        prompt = os.getcwd()
    else:
        print('Invalid directory.')
    

def store_configs():
    pass

def print_prompt():
    global colors
    global prompt
    global prompt_symbol
    print(colors.get('prompt') + prompt, end='')
    print(colors.get('prompt_symbol') + prompt_symbol, end='')


def run_function(cmd='$'):
    if(cmd == '$'):
        return 0

    cmd[0] = cmd[0][1:] # Removes the $ symbol

    if(cmd[0] == 'help'):
        print_help()
        return
    elif cmd[0] == 'ext':
        if(len(cmd) > 3):
            print('To many arguments.')
        elif cmd[1][0] != '.' or cmd[2][0] == '.':
            print('Invalid extension.')
        else:
            global execute_file
            execute_file[cmd[1]] = cmd[2]

    elif cmd[0] == 'store':
        store_configs()
    elif cmd[0] == 'path':
        add_path()
    else:
        print('Invalid command.')

def add_path():
    pass

def print_help():
    print('ext [extension] [name of the program to execute] - Saves the combination of pair extension and program to allow the files with the given extension to be executed.')
    print('store - Stores the configs currently present in the program. Will override the configs present in the files colors.conf, exec.conf and vars.conf.')
    print('path - Adds a new directory to search for executable files.')


def main():
    print('hello! Welcome to pyBash! Type help for more information.')
    
    while(1):
        print_prompt()
        cmd = input() # Holds the user input
        cmd = cmd.split()
        if(len(cmd) == 0):
            continue
        elif(cmd[0] == 'exit' or cmd[0] == 'q'):
            print('Bye!')
            break  
        elif(cmd[0] == 'cd'):
            change_dir(cmd[1:])
        
        elif(cmd[0][0] == '$'):
            run_function(cmd)
        else:
            execute_script(cmd[0], cmd[1:])

if __name__ == '__main__':
    try:

        # Add Function to work with argv
        # exec_argv():
        init(autoreset=True)
        main()
        deinit()
    except KeyboardInterrupt: # This is to not generate an error when you ctrl+c the program
        print()
    
    finally:
        deinit()


