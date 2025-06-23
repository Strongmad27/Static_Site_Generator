from blocktype import block_to_block_type, BlockType
from extract import extract_markdown_images, extract_markdown_links
from htmlnode import ParentNode, LeafNode, HTMLNode
from md_to_block import markdown_to_blocks
from split import split_nodes_delimiter, split_nodes_image, split_nodes_links
from text_to import text_to_textnodes
from textnode import TextNode, TextType
from md_to_html_node import markdown_to_html_node, raw_block_to_child_node, list_block_to_HTMLNode, hash_counter, blocktype_to_tag
import os, sys
import shutil
from copy_static_public import  public_clearing_house, copy_paste
from generate_web import generate_page, extract_title, generate_pages_recursive

def main():
    if len(sys.argv) >1:
        basepath = sys.argv[1]
    else:
        basepath = '/'
    public_clearing_house('docs')
    copy_paste('static', 'docs')
    generate_pages_recursive('content', 'template.html', 'docs', basepath)

  

if __name__ == "__main__":
    main()