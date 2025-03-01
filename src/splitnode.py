from textnode import *

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
                string_list.append(TextNode(current_text[delim_open+1:delim_closed], text_type))

                current_text = current_text[delim_closed+1:]

        else:
            #non-text nodes
            string_list.append(node)
    # print("*******")
    # print(string_list)
    # print("*******")
    return string_list

def find_delimiters(text, delimiter, start=0):
    delim_open = text.find(delimiter, start)
   
    if delim_open != -1:
        delim_close = text.find(delimiter, delim_open + 1)
    else:
        delim_close = -1

    if delim_open !=-1 and delim_close == -1:
        raise Exception("Invalid Markdown: No closing delimiter found.")

    return delim_open, delim_close

