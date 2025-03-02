from blockutils import *
from textnode import *
from leafnode import *
from parentnode import *
from htmlnode import *
from nodeutils import *
import pprint

def markdown_to_html_node(markdown):
    markdown_blocks = markdown_to_blocks(markdown)
    node_list = []
    for block in markdown_blocks:
        block_type = block_to_block_type(block)
        block_text = ""
        match (block_type):
            case BlockType.P:
                node = ParentNode("p", None, None)
                block_text = block
            case BlockType.HEADING:
                node = ParentNode("h1", None, None)
                block_text = block.lstrip("#")
            case BlockType.CODE_BLOCK:
                node = ParentNode("code", None, None)
                block_text = block[2:-2]
            case BlockType.QUOTE_BLOCK:
                node = ParentNode("blockquote", None, None)
                block_text = block.strip(">")
            case BlockType.UL:
                node = ParentNode("UL", None, None)
                block_text = block.strip("- ")
            case BlockType.OL:
                node = ParentNode("OL", None, None)
                block_text = block.strip("1. ")
            case _:
                node = node = ParentNode("p", None, None)
        node_list.append(node)
        text_to_children(block)

    # print("\n")
    # pprint.pp(node_list)
    # print("\n")
        # pprint.pp("**** LOOOP *****")
        # pprint.pp(block)
        # pprint.pp(block_type)

def text_to_children(text):
    print("THE CHIDREL!!!!!!!")
    print(text)
    #text_nodes = text_to_textnodes(text)
    #pprint.pp(text_nodes)