from blocktype import block_to_block_type, BlockType
from extract import extract_markdown_images, extract_markdown_links
from htmlnode import ParentNode, LeafNode, HTMLNode
from md_to_block import markdown_to_blocks
from split import split_nodes_delimiter, split_nodes_image, split_nodes_links
from text_to import text_to_textnodes
from textnode import TextNode, TextType
from md_to_html_node import markdown_to_html_node, raw_block_to_child_node, list_block_to_HTMLNode, hash_counter, blocktype_to_tag
import os
import shutil
from copy_static_public import  public_clearing_house, copy_paste
from generate_web import generate_page, extract_title

def main():
    public_clearing_house('public')
    copy_paste('static', 'public')
    generate_page('content/index.md', 'template.html', 'public/index.html')

  

if __name__ == "__main__":
    main()