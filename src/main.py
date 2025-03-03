import os

from generate_site import *

DEFAULT_SOURCE_STATIC_FOLDER = "./static"
DEFAULT_DEST_PUBLIC_FOLDER = "./public"
DEFAULT_SOURCE_CONTENT_FOLDER = "./content"
DEFAULT_TEMPLATE_PATH = "."

def main():
    print("Starting Static Site Generator")
    copy_files_static_to_public(DEFAULT_SOURCE_STATIC_FOLDER, DEFAULT_DEST_PUBLIC_FOLDER)
    generate_pages_recursive(DEFAULT_SOURCE_CONTENT_FOLDER, DEFAULT_TEMPLATE_PATH, DEFAULT_DEST_PUBLIC_FOLDER )

main()