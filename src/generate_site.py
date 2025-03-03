from blockutils import *
from convertutils import *
import re
import os


def extract_title(content):
    print(f"Reading Title from File:" )

    if len(content) == 0:
        raise Exception("No content provided")
    
    first_line = content.split("\n")[0]

    
    get_header = re.match(r"^#{1}[\w\d\s]+", first_line)
    
    if get_header == None:
        raise Exception("No level 1 header found at start!")
    
    header_text = first_line.lstrip("#").strip()
    print(f"Found Title: {header_text}")
    return header_text

def generate_page(from_path, template_path, dest_path):
    print(f"Generating file from {from_path} to {dest_path} using {template_path}")
    
    
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
    formated_content_title = formated_content_title.replace("{{ Content }}", html_content)

    new_html_file = open(f"{dest_path}", "x")
    new_html_file.write(formated_content_title)
    new_html_file.close()

    

    





