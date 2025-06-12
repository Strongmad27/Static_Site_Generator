import unittest
from blocktype import block_to_block_type, BlockType
from extract import extract_markdown_images, extract_markdown_links
from htmlnode import ParentNode, LeafNode, HTMLNode
from main import text_node_to_html_node
from md_to_block import markdown_to_blocks
from split import split_nodes_delimiter, split_nodes_image, split_nodes_links
from text_to import text_to_textnodes
from textnode import TextNode, TextType
from md_to_html_node import markdown_to_blocks, markdown_to_html_node, extract_markdown_images, extract_markdown_links, block_to_block_type, blocktype_to_tag, BlockType, raw_block_to_child_node, list_block_to_HTMLNode, split_nodes_delimiter, split_nodes_image, split_nodes_links, text_node_to_html_node, text_to_textnodes, TextNode, TextType, hash_counter, HTMLNode, LeafNode, ParentNode

class TestMDToHTML(unittest.TestCase):
    def test_paragraphs(self):
        md = """
    This is **bolded** paragraph
    text in a p
    tag here

    This is another paragraph with _italic_ text and `code` here

    """

        node = markdown_to_html_node(md)
        print(f'{node}')
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
    ```
    This is text that _should_ remain
    the **same** even with inline stuff
    ```
    """

        node = markdown_to_html_node(md)
        print(f'{node}')
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )