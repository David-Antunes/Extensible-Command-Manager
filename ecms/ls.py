
import os
from colorama import Fore
def main():
    print('This is all of the available scripts.')
    print('Type the name of the file and any necessary arguments.')
    p = os.listdir()
    for file in p:
        if(file[0] == '.'):
            print(Fore.RED + file)
        elif os.path.isdir(file):
            print(Fore.BLUE + file)
        else:
            print(Fore.GREEN + file)


if __name__ == "__main__":
    main()
