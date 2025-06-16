from extract import extract_markdown_images, extract_markdown_links
from split import split_nodes_links, split_nodes_delimiter, split_nodes_image
from textnode import TextNode, TextType
from main import text_node_to_html_node

def text_to_textnodes(text):
    text_node = TextNode(text, TextType.TEXT)
    nodes =[text_node]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_links(nodes)
    return nodes