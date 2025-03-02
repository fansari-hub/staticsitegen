from enum import Enum
import re

class BlockType(Enum):
    P = "paragraph"
    HEADING = "heading"
    CODE_BLOCK = "code"
    QUOTE_BLOCK = "quote"
    UL = "unordered_list"
    OL = "ordered_list"

def block_to_block_type(markdown_block):

    if (re.match(r"^#+ [\w\d\s]+", markdown_block)) != None:
        return BlockType.HEADING
    elif (re.match(r"^(```)[\w\d\s\*\.\\]+(```)$", markdown_block)) != None:
        return BlockType.CODE_BLOCK
    elif (re.match(r"^(?:>.*(?:\r?\n|$))+$", markdown_block)) != None:
        return BlockType.QUOTE_BLOCK
    elif (re.match(r"^(?:-\s.*(?:\r?\n|$))+$", markdown_block)) != None:
        return BlockType.UL
    elif (re.match(r"^(?:\d\..*(?:\r?\n|$))+$", markdown_block)) != None:
        return BlockType.OL
    else:
        return BlockType.P
    

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    new_blocks = []
    for block in blocks:
        text = block.strip()
        if len(text) > 0:
            new_blocks.append(text)
    return new_blocks


