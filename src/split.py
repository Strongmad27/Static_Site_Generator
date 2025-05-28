from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_node_list = []
    for node in old_nodes:
        node_text = node.text
        node_texttype = node.text_type
        split_node = node_text.split(delimiter)
        if node_texttype != TextType.TEXT:
            new_node_list.append(node)
            continue
        elif len(split_node) % 2 == 0:
            raise Exception ("delimiter not found")
        else:
            for index, words in enumerate(split_node):            
                if words == "":
                    continue
                if index % 2 != 0:
                    new_TextNode = TextNode(words, text_type)
                    new_node_list.append(new_TextNode)
                else:
                    new_TextNode = TextNode(words, TextType.TEXT)
                    new_node_list.append(new_TextNode)
    return new_node_list
                