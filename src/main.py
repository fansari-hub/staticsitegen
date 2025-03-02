from textnode import *
from htmlnode import *
from leafnode import *
from parentnode import *
from nodeutils import *


def main():
    #node = TextNode("This is `text` with a `code block` word", TextType.TEXT)
    #split_nodes_delimiter([node], "`", TextType.CODE)
    extract_markdown_images("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg")
    extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)")
    print("****")

main()