from pathlib import Path
import os
def readfileandfolder():
    try:
        p = Path("")
        items = list(p.rglob("*"))
        for  index , file in enumerate(items):
            print(f"{index}-{file}")
    except Exception as e:
        print(e)
def creat_file():
    try:
        readfileandfolder()
        file_name = input("enter your file name: ")
        p = Path("")
        if p.exists():
            print("file alrady exists")
        else:
            with open(file_name,"w") as file:
                content = input("enter your file content")
                file.write(content)
                print("file added")
    except Exception as e:
        print(e)
def read_file():
    try:
        readfileandfolder()
        file_name = input("enetr your file name: ")
        p = Path("")
        if p.exists():
            with open(file_name,"r") as file:
                print(file.read())
        else:
            print("file not exists")
    except Exception as e:
        print(e)
def update_file():
    try:
        readfileandfolder()
        file_name = input("enter your file name: ")
        p = Path(file_name)
        if p.exists():
            print("pass 1 to overwrite the content")
            print("pass 2 to overwrite the content")
            option = int(input("enter your choic for updating a file: "))
            if option == 1:
                with open(file_name,"w") as file:
                    content = input("enter your content")
                    file.write(content)
                    print("content, change....")
            else:
                print("invalid input")
    except Exception as e:
        print(e)
def delet_file():
    try:
        readfileandfolder()
        file_name = input('enetr your file name: ')
        p = Path(file_name)
        if p.exists():
            os.remove(p)
            print("file deleted")
        else:
            print("file does not ecsists")
    except Exception as e:
        print(e)
def rename_file():
    try:
        readfileandfolder()
        file_name = input("enter namr of your file: ")
        p = Path(file_name)
        if p.exists():
            new_file = input("enetr new file name: ")
            p.rename(new_file)
            print("file renamed!")
        else:
            print("file not found!")
    except Exception as e:
        print(e)
def creat_folder():
    readfileandfolder()
    folder_name = input("enter name of your folder: ")
    p = Path(folder_name)
    if p.exists():
        print("folder already exists!")
    else:
        p.mkdir()
        print("folder created!")
def delet_folder():
    readfileandfolder()
    folder_name = input("eneter name of your folder: ")
    p = Path(folder_name)
    if p.exists():
        p.rmdir()
        print("folder delet")
    else:
        print("folder not found")
def create_file_in_folder():
    folder_name = input("enetr name of your filder: ")
    file_name = input("enetr name of your file: ")
    p = Path(folder_name/file_name)
    if p.exists():
        print("file already exists")
    else:
        pass      
while True:
    print("press 1 for create a file: ")
    print("press 2 for read a file: ")
    print("press 3 update a file: ")
    print("press 4 delet a file: ")
    print("prass 5 rename a file: ")
    print("prass 6 for creating a folder: ")
    print("prass 7 for deleting a folder: ")
    print("preess 0 for exiting.......")
    option = int(input("enter your choice"))
    if option == 1:
        creat_file()
    if option == 2:
        read_file()
    if option == 3:
        update_file()
    if option == 4:
        delet_file
    if option == 5:
        rename_file()
    if option == 6:
        creat_folder()
    if option == 7:
        delet_folder()

    if option == 0:
        break