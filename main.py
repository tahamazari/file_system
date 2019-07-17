from functions import *

def main():
    while True:
        print("Choose from the following options")
        print("Press 1 to create a file")
        print("Press 2 to remove a file")
        print("Press 3 to read a file")
        print("Press 4 to append to a file")
        print("Press 5 to write to a file")
        print("Press 6 to search a string in the file")
        print("Press 7 to search a string in the file")
        print("Press 8 to search a string in the file")

        action = int(input())

        if(action == 1):
            create_file()
        elif(action == 2):
            remove_file()
        elif(action == 3):
            read_file()
        elif(action == 4):
            append_file()
        elif(action == 5):
            write_file()
        elif(action == 6):
            search_string()
        elif(action == 7):
            search_string()
        elif(action == 8):
            replace_string()
        else:
            exit()

main()