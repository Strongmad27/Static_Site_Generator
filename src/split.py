from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_node_list = []
    for node in old_nodes:
        if node.TextType != TextType.TEXT:
            raise Exception ("not a Text Node")
        if delimiter not in node:
            new_node_list.extend(node)
        new_node_split = node.split(delimiter)
        header = TextNode(new_node_split[0], TextType.TEXT)
        footer = TextNode(new_node_split[2], TextType.TEXT)
        text_code=""
        if delimiter == "'":
            text_code = TextType.CODE
        if delimiter == "**":
            text_code = TextType.BOLD
        if delimiter == "_":
            text_code = TextType.ITALIC
        body = TextNode(new_node_split[1], text_code)
        node_list = [header, body, footer]
        new_node_list.extend(node_list)



