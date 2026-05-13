import streamlit as st
from pathlib import Path
import os

st.title("📁 File Manager App")

# ---------- SHOW FILES ----------

st.subheader("Current Files & Folders")

p = Path(".")
items = list(p.rglob("*"))

for index, item in enumerate(items):
    st.write(f"{index} - {item}")

# ---------- INPUT ----------

name = st.text_input("Enter File/Folder Name")

content = st.text_area("Enter File Content")

# ---------- BUTTONS ----------

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Create File"):

        if Path(name).exists():
            st.warning("File already exists")

        else:
            with open(name, "w") as file:
                file.write(content)

            st.success("File Created")


with col2:
    if st.button("Read File"):

        if Path(name).exists():

            with open(name, "r") as file:
                st.text(file.read())

        else:
            st.error("File not found")


with col3:
    if st.button("Update File"):

        if Path(name).exists():

            with open(name, "w") as file:
                file.write(content)

            st.success("File Updated")

        else:
            st.error("File not found")


# ---------- DELETE FILE ----------

if st.button("Delete File"):

    if Path(name).exists():
        os.remove(name)
        st.success("File Deleted")

    else:
        st.error("File not found")


# ---------- CREATE FOLDER ----------

if st.button("Create Folder"):

    p = Path(name)

    if p.exists():
        st.warning("Folder already exists")

    else:
        p.mkdir()
        st.success("Folder Created")


# ---------- DELETE FOLDER ----------

if st.button("Delete Folder"):

    p = Path(name)

    if p.exists():
        p.rmdir()
        st.success("Folder Deleted")

    else:
        st.error("Folder not found")