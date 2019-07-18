import os

def create_file():
    print("Type in name of file and its extension you want to create")
    name = input()
    if file_exists(name):
        print("file already exists")
        return
    file = open(name, "w+")

def remove_file():
    print("Type in name of file and its extension you want to remove")
    name = input()
    if not file_exists(name):
        return
    os.remove(name)

def read_file():
    print("Type name of file you want to read")
    name = input()
    if not file_exists(name):
        return
    file = open(name, "r")
    print(file.read())
    file.close()

def change_file(m):
    print("Type name of file you want to change")
    name = input()
    if not file_exists(name):
        return
    print("Type what you want to append to file")
    data = input()
    f = open(name, m)
    f.write(data)
    f.close()

def search_string():
    print("Type name of file you want to search")
    name = input()
    if not file_exists(name):
        return
    print("Type in string you want to check")
    search = input()
    with open(name,'r') as file:
        if search in file.read():
            print("String " + search + " was found")
        else:
            print("String not found")
    file.close()

def replace_string():
    print("Type name of file in which you want to replace")
    name = input()
    if not file_exists(name):
        return
    print("Type string you want to replace")
    current = input()
    print("Type string you want to replace it with")
    new = input()
    fin = open(name, "r")
    data = fin.read()
    data = data.replace(current, new)
    fin.close()

    fin = open(name, "w")
    fin.write(data)
    fin.close()

def file_exists(file):
    if not os.path.isfile(file):
        print("file not found")
        return False
    return True