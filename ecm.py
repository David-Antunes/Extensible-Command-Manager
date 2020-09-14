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
colors = {
    'prompt' : Fore.GREEN,
    'prompt_symbol' : Fore.BLUE,
}

# Extensions the program recognizes and will try to execute
execute_file = {}


# initial values
# delete after config files are done

prompt = os.getcwd()
prompt_symbol = ':$ '
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
        print(ph)
        prog_list = os.listdir(ph)
        print(prog_list)
        for prog in prog_list:
            if prog == filename:
                return os.path.realpath(ph + '/' + filename)


def change_dir(cmd = []):
    if cmd == []:
        print('Not enough arguments. Provide a directory name after cd.')
        return

    elif len(cmd) > 1:
        print('To many arguments.')
        return
    
    elif cmd[1] == '--h':
        print('cd [Directory name] or [absolute Path ex: /home/example]')
        return

    global prompt
    os.chdir(cmd)
    prompt = os.getcwd()
    

def store_configs():
    pass

def print_prompt():
    global colors
    global prompt
    global prompt_symbol
    print(colors.get('prompt') + prompt, end='')
    print(colors.get('prompt_symbol') + prompt_symbol, end='')


def main():
    print('hello! Welcome to pyBash! Type help for more information.')
    
    while(1):
        print_prompt()
        cmd = input() # Holds the user input
        cmd = cmd.split()

        if(cmd[0] == 'exit' or cmd[0] == 'q'):
            print('Bye!')
            break  
        elif(cmd[0] == 'cd'):
            change_dir(cmd[1:])
            

        elif(cmd == 'ecm store configs'):
            store_configs()

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


