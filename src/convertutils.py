from blockutils import *
from textnode import *
from leafnode import *
from parentnode import *
from htmlnode import *
from nodeutils import *
import pprint

def markdown_to_html_node(markdown):
    markdown_blocks = markdown_to_blocks(markdown)
    top_html_node = ParentNode("div", None, None)
    block_html_nodes = []

    for block in markdown_blocks:
        block_type = block_to_block_type(block)
        block_html_node = map_block_to_html_node(block_type, block)
        block_text_stripped = strip_markup(block, block_type)
        
        if block_type != BlockType.CODE_BLOCK:
            block_html_node.children = text_to_children(block_text_stripped)
        else:
            block_html_node.children[0].children = [LeafNode(tag=None, value=f"{block_text_stripped}")]
        
        block_html_nodes.append(block_html_node)

    top_html_node.children = block_html_nodes
    return top_html_node

def map_block_to_html_node(block_type, block):
        match (block_type):
            case BlockType.P:
                node = ParentNode("p", None, None)
            case BlockType.HEADING:
                node = ParentNode(map_block_header_tag(block), None, None)
            case BlockType.CODE_BLOCK:
                node_c = ParentNode("code", None, None)
                node = ParentNode("pre", children=[node_c], prop=None)
            case BlockType.QUOTE_BLOCK:
                node = ParentNode("blockquote", None, None)
            case BlockType.UL:
                node = ParentNode("ul", None, None)
            case BlockType.OL:
                node = ParentNode("ol", None, None)
            case _:
                node = node = ParentNode("p", None, None)
        return node

def strip_markup(block, block_type):
    block_body_text = ""
    match (block_type):
        case BlockType.P:
            block_body_text = block.replace("\n", "<BR/>")
        case BlockType.HEADING:
            block_body_text = block.lstrip("#").replace("\n", "<BR/>")
        case BlockType.CODE_BLOCK:
            block_body_text = block[3:-3]
        case BlockType.QUOTE_BLOCK:
            block_body_text = split_and_strip(block, ">", False, "<BR/>")
        case BlockType.UL:
            block_body_text = split_and_strip(block, "- ", False, "<BR/>", "li")
        case BlockType.OL:
            block_body_text = split_and_strip(block, ".", True, "<BR/>",  "li")
        case _:
            raise Exception("Did not find valid block type!")
    return block_body_text

def split_and_strip(block, markup, counterType=False, newLine="\n", multi_line_tag = None):
    multi_lines = block.split("\n")
    new_lines = []
    
    for line in multi_lines:
        if (counterType ==  False):
            current_line = line.replace(markup, "")
            new_lines.append(current_line)
        else:
            current_line = line.split(markup, 1)[1]
            new_lines.append(current_line)

    if multi_line_tag == None:
        return f"{newLine}".join(new_lines)
    else:
        new_lines_2 = []
        for line in new_lines:
            new_lines_2.append(f"<{multi_line_tag}>{line}</{multi_line_tag}>")
        return "".join(new_lines_2)
        
def map_block_header_tag(block):
    if block.startswith("######"):
        return "h6"
    elif block.startswith("#####"):
        return "h5"
    elif block.startswith("####"):
        return "h4"
    elif block.startswith("###"):
        return "h3"
    elif block.startswith("##"):
        return "h2"
    elif block.startswith("#"):
        return "h1"
    else:
        raise Exception("This is not a header block!")
    
def text_to_children(text):
        children_nodes = text_to_textnodes(text)
        child_html_nodes = []
        for child in children_nodes:
            child_html_nodes.append(text_node_to_html_node(child))
        return child_html_nodes