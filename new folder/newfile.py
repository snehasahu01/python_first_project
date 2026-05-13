import streamlit as st
from pathlib import Path
import os

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="CRUD File Manager",
    page_icon="📁",
    layout="centered"
)

st.title("📁 CRUD File Manager")

# ---------------- SHOW FILES ---------------- #

st.subheader("📂 Current Files & Folders")

p = Path('.')
items = list(p.rglob('*'))

if items:
    for index, item in enumerate(items):
        st.write(f"{index + 1} - {item}")
else:
    st.info("No files or folders found.")

st.divider()

# ---------------- CREATE FILE ---------------- #

st.subheader("📝 Create File")

create_file_name = st.text_input(
    "Enter file name",
    key="create_file"
)

create_content = st.text_area(
    "Enter file content",
    key="create_content"
)

if st.button("Create File"):

    p = Path(create_file_name)

    if p.exists():
        st.error("File already exists!")

    else:
        try:
            with open(create_file_name, 'w', encoding='utf-8') as file:
                file.write(create_content)

            st.success("File created successfully!")
        except Exception as e:
            st.error(f"Error creating file: {str(e)}")

# ---------------- READ FILE ---------------- #

st.divider()

st.subheader("📖 Read File")

read_file_name = st.text_input(
    "Enter file name to read",
    key="read_file"
)

if st.button("Read File"):

    p = Path(read_file_name)

    if p.exists():
        try:
            with open(read_file_name, 'r', encoding='utf-8') as file:
                content = file.read()

            st.text_area(
                "File Content",
                content,
                height=200
            )
        except Exception as e:
            st.error(f"Error reading file: {str(e)}")

    else:
        st.error("File not found!")

# ---------------- UPDATE FILE ---------------- #

st.divider()

st.subheader("✏️ Update File")

update_file_name = st.text_input(
    "Enter file name to update",
    key="update_file"
)

update_content = st.text_area(
    "Enter new content",
    key="update_content"
)

if st.button("Update File"):

    p = Path(update_file_name)

    if p.exists():
        try:
            with open(update_file_name, 'w', encoding='utf-8') as file:
                file.write(update_content)

            st.success("File updated successfully!")
        except Exception as e:
            st.error(f"Error updating file: {str(e)}")

    else:
        st.error("File not found!")

# ---------------- DELETE FILE ---------------- #

st.divider()

st.subheader("🗑️ Delete File")

delete_file_name = st.text_input(
    "Enter file name to delete",
    key="delete_file"
)

if st.button("Delete File"):

    p = Path(delete_file_name)

    if p.exists():

        os.remove(p)

        st.success("File deleted successfully!")

    else:
        st.error("File not found!")

# ---------------- CREATE FOLDER ---------------- #

st.divider()

st.subheader("📁 Create Folder")

folder_name = st.text_input(
    "Enter folder name",
    key="folder_name"
)

if st.button("Create Folder"):

    p = Path(folder_name)

    if p.exists():
        st.error("Folder already exists!")

    else:
        p.mkdir()

        st.success("Folder created successfully!")

# ---------------- DELETE FOLDER ---------------- #

st.divider()

st.subheader("❌ Delete Folder")

delete_folder_name = st.text_input(
    "Enter folder name to delete",
    key="delete_folder"
)

if st.button("Delete Folder"):

    p = Path(delete_folder_name)

    if p.exists():

        try:
            p.rmdir()
            st.success("Folder deleted successfully!")

        except OSError:
            st.error("Folder is not empty!")

    else:
        st.error("Folder not found!")