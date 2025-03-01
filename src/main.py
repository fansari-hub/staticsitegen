from textnode import *
from htmlnode import *
from leafnode import *
from parentnode import *
from splitnode import *


def main():
    node = TextNode("This is `text` with a `code block` word", TextType.TEXT)
    split_nodes_delimiter([node], "`", TextType.CODE)

main()