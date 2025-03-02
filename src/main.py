import os
import shutil
import pprint

DEFAULT_SOURCE_STATIC_FOLDER = "./static"
DEFAULT_DEST_PUBLIC_FOLDER = "./public"


def copy_files_static_to_public(source_folder=DEFAULT_SOURCE_STATIC_FOLDER, dest_folder=DEFAULT_DEST_PUBLIC_FOLDER):
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
    


def main():
    print("Starting Static Site Genetor")
    copy_files_static_to_public()

main()