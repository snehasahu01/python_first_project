from tkinter import *
from tkinter import filedialog, messagebox
from pathlib import Path
import os

root = Tk()
root.title("File Manager")
root.geometry("600x500")

# ---------- FUNCTIONS ----------

def list_items():
    listbox.delete(0, END)
    p = Path(".")
    items = list(p.rglob("*"))

    for index, item in enumerate(items):
        listbox.insert(END, f"{index} - {item}")


def create_file():
    file_name = entry.get()

    if Path(file_name).exists():
        messagebox.showinfo("Info", "File already exists")
    else:
        with open(file_name, "w") as file:
            file.write(text.get("1.0", END))

        messagebox.showinfo("Success", "File Created")
        list_items()


def read_file():
    file_name = entry.get()

    if Path(file_name).exists():
        with open(file_name, "r") as file:
            content = file.read()

        text.delete("1.0", END)
        text.insert(END, content)

    else:
        messagebox.showerror("Error", "File not found")


def update_file():
    file_name = entry.get()

    if Path(file_name).exists():
        with open(file_name, "w") as file:
            file.write(text.get("1.0", END))

        messagebox.showinfo("Success", "File Updated")

    else:
        messagebox.showerror("Error", "File not found")


def delete_file():
    file_name = entry.get()

    if Path(file_name).exists():
        os.remove(file_name)
        messagebox.showinfo("Success", "File Deleted")
        list_items()

    else:
        messagebox.showerror("Error", "File not found")


def create_folder():
    folder_name = entry.get()

    p = Path(folder_name)

    if p.exists():
        messagebox.showinfo("Info", "Folder already exists")
    else:
        p.mkdir()
        messagebox.showinfo("Success", "Folder Created")
        list_items()


def delete_folder():
    folder_name = entry.get()

    p = Path(folder_name)

    if p.exists():
        p.rmdir()
        messagebox.showinfo("Success", "Folder Deleted")
        list_items()

    else:
        messagebox.showerror("Error", "Folder not found")


# ---------- UI ----------

Label(root, text="Enter File/Folder Name", font=("Arial", 14)).pack(pady=10)

entry = Entry(root, width=40, font=("Arial", 12))
entry.pack()

text = Text(root, height=10, width=60)
text.pack(pady=10)

Frame1 = Frame(root)
Frame1.pack()

Button(Frame1, text="Create File", command=create_file).grid(row=0, column=0, padx=5)
Button(Frame1, text="Read File", command=read_file).grid(row=0, column=1, padx=5)
Button(Frame1, text="Update File", command=update_file).grid(row=0, column=2, padx=5)

Frame2 = Frame(root)
Frame2.pack(pady=10)

Button(Frame2, text="Delete File", command=delete_file).grid(row=0, column=0, padx=5)
Button(Frame2, text="Create Folder", command=create_folder).grid(row=0, column=1, padx=5)
Button(Frame2, text="Delete Folder", command=delete_folder).grid(row=0, column=2, padx=5)

Button(root, text="Refresh Files", command=list_items).pack(pady=10)

listbox = Listbox(root, width=80, height=10)
listbox.pack()

list_items()

root.mainloop()