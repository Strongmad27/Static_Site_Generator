from extract import extract_markdown_images, extract_markdown_links
from split import split_nodes_links, split_nodes_delimiter, split_nodes_image
from textnode import TextNode, TextType
from main import text_node_to_html_node

def text_to_textnodes(text):
    text_node = TextNode(text, TextType.TEXT)
    node_list=[text_node,]
    return split_nodes_links(split_nodes_image(split_nodes_delimiter(split_nodes_delimiter(split_nodes_delimiter(node_list, "**", TextType.BOLD), "_", TextType.ITALIC), "`", TextType.CODE)))
