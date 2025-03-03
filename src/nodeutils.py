from textnode import *
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    string_list = []
    
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            
            current_text = node.text
            while True:
                delim_open, delim_closed = find_delimiters(current_text, delimiter)

                #No more delimiters left to process
                if delim_open == -1:
                    if current_text != "":
                        string_list.append(TextNode(current_text, TextType.TEXT))
                    break
                
                #append text before the delimiter
                if delim_open > 0:
                    string_list.append(TextNode(current_text[0:delim_open], TextType.TEXT))
                    
                #apend text inside delimiter
                string_list.append(TextNode(current_text[delim_open+len(delimiter):delim_closed], text_type))

                current_text = current_text[delim_closed+len(delimiter):]

        else:
            #non-text nodes
            string_list.append(node)
    return string_list

def split_nodes_image(old_nodes):
    node_list = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            current_text = node.text
            while True:
                delim_open, delim_closed = find_delimiters(current_text, "!", ")", no_missing_end_delimiter_assert=True)

                #Not a image delimiter, just use of same character in text, ignore
                if delim_closed == -2:
                    node_list.append(TextNode(current_text, TextType.TEXT))
                    #node_list.append(node)
                    break

                #No more delimiters left to process
                if delim_open == -1:
                    if current_text != "":
                        node_list.append(TextNode(current_text, TextType.TEXT))
                    break
                  
                #append text before the delimiter
                if delim_open > 0:
                    node_list.append(TextNode(current_text[0:delim_open], TextType.TEXT))
                    
                #append text inside delimiter
                result = extract_markdown_images(current_text[delim_open:delim_closed+1])

                #Need to check for this if it false delimiters were found
                image_alt , image_url = result[0]

                node_list.append(TextNode(image_alt, TextType.IMAGE, image_url))
                current_text = current_text[delim_closed+1:]
        
        else:
            #non-text nodes
            node_list.append(node)
    return node_list
        
def split_nodes_link(old_nodes):
    node_list = []

    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            current_text = node.text
            while True:
                delim_open, delim_closed = find_delimiters(current_text, "[", ")", no_missing_end_delimiter_assert=True)


                #Not a link delimiter, just use of same character in text, ignore
                if delim_closed == -2:
                    node_list.append(TextNode(current_text, TextType.TEXT))
                    break

                #No more delimiters left to process
                if delim_open == -1:
                    if current_text != "":
                        node_list.append(TextNode(current_text, TextType.TEXT))
                    break
                  
                #append text before the delimiter
                if delim_open > 0:
                    node_list.append(TextNode(current_text[0:delim_open], TextType.TEXT))
                    
                #append text inside delimiter
                result = extract_markdown_links(current_text[delim_open:delim_closed+1])
                link_txt , link_url = result[0]
                node_list.append(TextNode(link_txt, TextType.LINK, link_url))
                current_text = current_text[delim_closed+1:]
        
        else:
            #non-text nodes
            node_list.append(node)
    return node_list

def find_delimiters(text, delimiter_a, delimiter_b=None, start=0, no_missing_end_delimiter_assert=False):
    if delimiter_b == None:
        delimiter_b = delimiter_a
    delim_open = text.find(delimiter_a, start)
   
    if delim_open != -1:
        delim_close = text.find(delimiter_b, delim_open + len(delimiter_a))
    else:
        delim_close = -1

    if delim_open !=-1 and delim_close == -1:
        if no_missing_end_delimiter_assert == False:
            raise Exception("Invalid Markdown: No closing delimiter found.")
        return (-2, -2)

    return delim_open, delim_close

def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches
    
def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def text_to_textnodes(text):
    node = TextNode(text, TextType.TEXT)
    nodes1 = split_nodes_delimiter([node], "**", TextType.BOLD)
    nodes2 = split_nodes_delimiter(nodes1, "_", TextType.ITALIC)
    nodes3 = split_nodes_delimiter(nodes2, "`", TextType.CODE)
    nodes4 = split_nodes_image(nodes3)
    nodes5 = split_nodes_link(nodes4)
    return nodes5