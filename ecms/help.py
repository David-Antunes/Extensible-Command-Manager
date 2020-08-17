
import os

def main():
    print('This is all of the available scripts.')
    print('Type the name of the file and any necessary arguments.')
    p = os.listdir()
    for file in p:
        print(file)


if __name__ == "__main__":
    main()
