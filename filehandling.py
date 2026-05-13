# project - CRUD opretion
# 1 try
# 2 except
from pathlib import Path
import os
def readfileandfolder():
    try:
        p = Path('') 
        items = list(p.rglob('*'))
        for index , file in enumerate(items):
            print(f'{index} - {file}')
    except Exception as e:
        print(e)        
def create_file():
    try:
        readfileandfolder()
        file_name = input('enter name of your file: ')
        p = Path(file_name)
        if p.exists():
            print('file alredy exists')
        else:
            with open(file_name,'w') as file:
                content = input("enter your file content: ")
                file.write(content)
                print('file added!')
    except Exception as e:
        print(e) 
def read_file():
    try:
        readfileandfolder()
        file_name = input("enter name of your file: ")
        p = Path(file_name)
        if p.exists():
            with open(file_name,'r') as file:
                print(file.read())
        else:
            print('file not found!')
    except Exception as e:
        print(e)
def update_file():
    try:
        readfileandfolder()
        file_name = input("enter name of your file: ")
        p = Path(file_name)
        if p.exists():
            print('prss 1 to overwrite the content')
            print('press 2 to append new content')
            option = int(input("enter your choice for updating a file: "))
            if option ==1:
                with open(file_name,"w") as file:
                    content = input("enetr your content: ")
                    file.write(content)
                    print("content changed...")

            elif option == 2:
                with open(file_name,"a") as file:
                    content = input("enter your content: ")
                    file.write(content)
                    print("content change.... ")
            else:
                print("invalid input")
    except Exception as e:
        print(e)     
def delet_file():
    try:
        readfileandfolder()
        file_name = input("enter your file name: ")
        p = Path(file_name)
        if p.exists():
            os.remove(p)# os is remobing path of that file completely from the system
            print("file deleted")
        else:
            print("file does not exists")
    except Exception as e:
        print(e)
while True:
    print("prass 1 for creating a file")
    print("prass 2 for reading a file")
    print("prass 3 for updating a file")
    print("prass 4 for deleting a file")
    print(" press 0 for exiting")
    option = int(input("enter your choice"))
    if option ==1:
        create_file()
        
    if option ==2:
        read_file()  
    if option ==3:
        update_file()
        
    if option ==4:
        delet_file()
        
    if option == 0:
        break