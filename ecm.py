import os
import sys
import pathlib as pl
import subprocess

# Displays the prompt in the pyBash
prompt = ''

# Directories to verify if there is a corresponding script to be executed
path = []

# Structure of colors inside the pyBash
colors = []

# Extensions the program recognizes and will try to execute
execute_file = {}


# initial values
# delete after config files are done

prompt = os.getcwd() + ':$ '
path = [os.getcwd() + '/ecms',]
execute_file = {
    '.py' : 'python3',
}

def execute_script(cmd='',args=[]):
    if(cmd == ''):
        print()
    else:
        extension = get_file_extension(cmd)
        if extension in execute_file:

            subprocess.run([execute_file.get(extension), cmd + extension + ''.join(args)])
        else:
            print('No script with that name.')

def get_file_extension(cmd=''):

    for ph in path:
        prog_list = os.listdir(ph)
        for prog in prog_list:
            prog = prog.split('.')
            if prog[0] == cmd:
                return prog[-1]
        
    return ''

def change_dir(cmd = ''):
    pass

def store_configs():
    pass



def main():
    print('hello! Welcome to pyBash! Type help for more information.')
    
    while(1):
        cmd = input(prompt) # Holds the user input
        cmd.split()

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

        main()
    except KeyboardInterrupt: # This is to not generate an error when you ctrl+c the program
        print()


