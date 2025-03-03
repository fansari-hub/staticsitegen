import sys

from generate_site import *

basepath = "/"
if len(sys.argv) > 1:
    basepath = sys.argv[1]


DEFAULT_SOURCE_STATIC_FOLDER = f"./static"
DEFAULT_DEST_PUBLIC_FOLDER = f"./docs"
DEFAULT_SOURCE_CONTENT_FOLDER = f"./content"
DEFAULT_TEMPLATE_PATH = f"."


def main():
    print("Starting Static Site Generator")
    print(f"Base HTTP server basepath= {basepath}")
    copy_files_static_to_public(DEFAULT_SOURCE_STATIC_FOLDER, DEFAULT_DEST_PUBLIC_FOLDER)
    print("\nStarting to generate pages for site....")
    generate_pages_recursive(DEFAULT_SOURCE_CONTENT_FOLDER, DEFAULT_TEMPLATE_PATH, DEFAULT_DEST_PUBLIC_FOLDER, basepath )

main()