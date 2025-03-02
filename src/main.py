from textnode import *
from htmlnode import *
from leafnode import *
from parentnode import *
from nodeutils import *


def main():
    #node = TextNode("This is `text` with a `code block` word", TextType.TEXT)
    #split_nodes_delimiter([node], "`", TextType.CODE)
    #node = TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)", TextType.TEXT)
    #print(split_nodes_image([node]))
    #node1 = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.TEXT)
    #print(split_nodes_link([node1]))
    #extract_markdown_images("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg")
    #extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)")
    text_to_textnodes()
    print("****")

main()