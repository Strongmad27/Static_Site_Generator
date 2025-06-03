from extract import extract_markdown_images, extract_markdown_links
from split import split_nodes_links, split_nodes_delimiter, split_nodes_image
from textnode import TextNode, TextType
from main import text_node_to_html_node

def text_to_textnodes(text):
    text_node = TextNode(text, TextType.TEXT)
    nodes =[text_node]
    print(f"Debug: Initial node.text = {text_node.text}, type = {type(text_node.text)}")
    print(f"Debug: Initial node type = {type(text_node)}")
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    print(f"After bold split: {nodes}")
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    print(f"After italics split: {nodes}") 
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    print(f"After code split: {nodes}")
    nodes = split_nodes_image(nodes)
    print(f"After image split: {nodes}")
    nodes = split_nodes_links(nodes)
    print(f"After links split: {nodes}")
    return nodes