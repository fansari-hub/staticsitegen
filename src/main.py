import os
import shutil
from generate_site import *

DEFAULT_SOURCE_STATIC_FOLDER = "./static"
DEFAULT_DEST_PUBLIC_FOLDER = "./public"
DEFAULT_SOURCE_CONTENT_FOLDER = "./content"
DEFAULT_TEMPLATE_PATH = "."


def copy_files_static_to_public(source_folder, dest_folder):
    if not os.path.exists(source_folder):
        raise Exception("STATIC folder does not exist!!")
    
    if not os.path.exists(dest_folder):
        raise Exception("PUBLIC folder does not exist!!")
    
    pubic_folder_files = os.listdir(dest_folder)

#Delete Files
    for item in pubic_folder_files:
        file_path = os.path.join(dest_folder, item)
        if os.path.isfile(file_path):
            print(f"Deleting file: {file_path}")
            os.remove(file_path)
        elif os.path.isdir(file_path):
            print(f"Deleting folder and contents: {file_path}")
            shutil.rmtree(file_path)

#Copy files
    print(f"Copying files from {source_folder} to {dest_folder}")
    shutil.copytree(source_folder, dest_folder, dirs_exist_ok=True)

def generate_files(source_file, template_file,  dest_file):
    source_path = os.path.join(DEFAULT_SOURCE_CONTENT_FOLDER, source_file)
    template_path = os.path.join(DEFAULT_TEMPLATE_PATH, template_file)
    dest_path = os.path.join(DEFAULT_DEST_PUBLIC_FOLDER, dest_file)
    generate_page(source_path, template_path, dest_path)

def main():
    print("Starting Static Site Genetor")
    copy_files_static_to_public(DEFAULT_SOURCE_STATIC_FOLDER, DEFAULT_DEST_PUBLIC_FOLDER)
    generate_files("index.md", "template.html", "index.html")

main()