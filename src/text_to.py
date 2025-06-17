from split import split_nodes_links, split_nodes_delimiter, split_nodes_image
from textnode import TextNode, TextType
from htmlnode import LeafNode

def text_to_textnodes(text):
    text_node = TextNode(text, TextType.TEXT)
    nodes =[text_node]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_links(nodes)
    return nodes

def text_node_to_html_node(text_node):
    if isinstance(text_node, TextNode):
        if text_node.text_type == TextType.TEXT:
            return LeafNode(None, text_node.text)
        if text_node.text_type == TextType.BOLD:
            return LeafNode("b", text_node.text)
        if text_node.text_type == TextType.ITALIC:
            return LeafNode("i", text_node.text)
        if text_node.text_type == TextType.CODE:
            return LeafNode("code", text_node.text)
        if text_node.text_type == TextType.LINK:
            return LeafNode("a", text_node.text, {'href': text_node.url})
        if text_node.text_type == TextType.IMAGE:
            return LeafNode("img", "", {"alt": text_node.text,
                                          "src": text_node.url
                                          } )
    raise Exception ("Text Type not found in class ENUM")  