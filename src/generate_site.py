from blockutils import *
from convertutils import *
import shutil
import re
import os
import pprint

def copy_files_static_to_public(source_folder, dest_folder):
    if not os.path.exists(source_folder):
        raise Exception("STATIC folder does not exist!!")
    
    if not os.path.exists(dest_folder):
        raise Exception("PUBLIC folder does not exist!!")
    
    pubic_folder_files = os.listdir(dest_folder)

    #Delete Files
    print("\nDeleting existing files in public folder...")

    for item in pubic_folder_files:
        file_path = os.path.join(dest_folder, item)
        if os.path.isfile(file_path):
            print(f"Deleting file: {file_path}")
            os.remove(file_path)
        elif os.path.isdir(file_path):
            print(f"Deleting folder and all sub-folders: {file_path}")
            shutil.rmtree(file_path)

#Copy files
    print(f"\nCopying all files from {source_folder} to {dest_folder}...")
    shutil.copytree(source_folder, dest_folder, dirs_exist_ok=True)

def extract_title(content):

    if len(content) == 0:
        raise Exception("No content provided")
    
    first_line = content.split("\n")[0]

    
    get_header = re.match(r"^#{1}[\w\d\s]+", first_line)
    
    if get_header == None:
        raise Exception("No level 1 header found at start!")
    
    header_text = first_line.lstrip("#").strip()
    print(f"Found file title: {header_text}\n")
    return header_text

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating file from {from_path} --> {dest_path} using {template_path}")
    
    
    markdown_file = open(from_path)
    markdown_content = markdown_file.read()
    markdown_file.close()
    file_title = extract_title(markdown_content)
    template_file = open(template_path)
    template_content = template_file.read()
    template_file.close()

    html_node = markdown_to_html_node(markdown_content)
    html_content = html_node.to_html()

    formated_content_title = template_content.replace("{{ Title }}", file_title)
    formated_content_body = formated_content_title.replace("{{ Content }}", html_content)
    formated_content_body_server = formated_content_body.replace('href="/', f'href="{basepath}').replace('src="/', f'src="{basepath}')

    new_html_file = open(f"{dest_path}", "x")
    new_html_file.write(formated_content_body_server)
    new_html_file.close()

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    if not os.path.exists(dir_path_content):
        raise Exception("source path does not exist!!")
    
    if not os.path.exists(dest_dir_path):
        raise Exception("destination path does not exist!!")
    
    if not os.path.exists(template_path):
        raise Exception("template path does not exist!!")
    
    content_folder_files = os.listdir(dir_path_content)

    for item in content_folder_files:
        file_path = os.path.join(dir_path_content, item)
        dest_path = os.path.join(dest_dir_path, item.split(".")[0] + ".html")
        template_file = os.path.join(template_path, "template.html")
        if os.path.isfile(file_path):
            print(f"Found file: {file_path}")
            generate_page(file_path, template_file, dest_path, basepath)
        elif os.path.isdir(file_path):
            print(f"Found folder: {file_path}")
            dir_path_content_next = file_path
            dest_dir_path_next = os.path.join(dest_dir_path, item)
            print(f"Creating destination folder: {dest_dir_path_next}")
            os.mkdir(dest_dir_path_next)
            generate_pages_recursive(dir_path_content_next, template_path, dest_dir_path_next, basepath)
    return None


    





