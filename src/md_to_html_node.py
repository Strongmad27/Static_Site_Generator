from blocktype import block_to_block_type, BlockType
from extract import extract_markdown_images, extract_markdown_links
from htmlnode import ParentNode, LeafNode, HTMLNode
from main import text_node_to_html_node
from md_to_block import markdown_to_blocks
from split import split_nodes_delimiter, split_nodes_image, split_nodes_links
from text_to import text_to_textnodes
from textnode import TextNode, TextType

##takes full markdown document and returns single parent node containg everything split into leaf nodes

       

def markdown_to_html_node(markdown):
    blocked_markdown_list = markdown_to_blocks(markdown)

    ## created list of markdown blocks to iterate over, determine types, then convert to HTMLNodes
    html_nodes = []
    for block in blocked_markdown_list:
        blocktype = block_to_block_type(block)
        ##referencing blocktype, create HTMLNode from the block
        if blocktype != BlockType.CODE:
            TN_list = text_to_textnodes(block)
            leaf_list=[]
            for node in TN_list:
                new_HN = text_node_to_html_node(node)
                leaf_list.append(new_HN)
            block_tag = blocktype_to_tag(blocktype, block)
            if blocktype == BlockType.UNORDERED_LIST:
                ul_leafs = []
                for ul_item in leaf_list:
                    ul_list = []
                    ul_list.append(ul_item)
                    ul_leaf = ParentNode('<li>', ul_list)
                    ul_leafs.append(ul_leaf)
                new_ul_node = ParentNode(block_tag, ul_leafs)
                html_nodes.append(new_ul_node)
            if blocktype == BlockType.ORDERED_LIST:
                ol_leafs = []
                for ol_item in leaf_list:
                    ol_list = []
                    ol_list.append(ol_item)
                    ol_leaf = ParentNode('<li>', ol_list)
                    ol_leafs.append(ol_leaf)
                new_ol_node = ParentNode(block_tag, ol_leafs)
                html_nodes.append(new_ol_node)
            if blocktype == BlockType.QUOTE:
                qu_leafs = []
                for qu_item in leaf_list:
                    qu_leaf = LeafNode(None, qu_item)
                    qu_leafs.append(qu_leaf)
                new_qu_node = ParentNode(block_tag, None, qu_leafs)
                html_nodes.append(new_qu_node)
            if blocktype == BlockType.HEADING:
                he_leafs = []
                fir_str = leaf_list[0]
                if block_tag == '<h1>':
                    fir_str = fir_str[-2]
                elif block_tag == '<h2>':
                    fir_str = fir_str[-3]
                elif block_tag == '<h3>':
                    fir_str = fir_str[-4]
                elif block_tag == '<h4>':
                    fir_str = fir_str[-5]
                elif block_tag == '<h5>':
                    fir_str = fir_str[-6]
                elif block_tag == '<h6>':
                    fir_str = fir_str[-7]
                leaf_list[0] = fir_str
                for he_item in leaf_list:
                    he_leaf = LeafNode(None, he_item)
                    he_leafs.append(he_leaf)
                new_he_par = ParentNode(block_tag, None, he_leafs)
                html_nodes.append(new_he_par)
            if blocktype == BlockType.PARAGRAPH:
                pa_leafs = []
                for pa_item in leaf_list:
                    pa_leaf = LeafNode(None, pa_item)
                    pa_leafs.append(pa_leaf)
                new_pa_node = ParentNode(block_tag, None, pa_leafs)
                html_nodes.append(new_pa_node)
        if blocktype == BlockType.CODE:
            code_text_list = block.splitlines()
            code_text_list = code_text_list[1:-1]
            new_line = '\n'
            code_text = new_line.join(code_text_list)
            new_leaf = [LeafNode(None, code_text),]
            co_leafs = [ParentNode('code', None, new_leaf)]
            new_code_par = ParentNode('pre', None, co_leafs)
            html_nodes.append(new_code_par) 
    big_bad_parent = ParentNode('div', None, html_nodes)
    return big_bad_parent

##helper functions below:

def hash_counter(block):
    hash = '#'
    i = 0
    length = max(7, len(block))
    for i in range(0, length):
        if block[i] == hash:
            i += 1
        elif block[i] == ' ':
            return f'<h{i}>'

def blocktype_to_tag(blocktype, block):
    if blocktype == BlockType.PARAGRAPH:
        block_tag = '<p>'
        return block_tag
    
    if blocktype == BlockType.HEADING:
        block_tag = hash_counter(block[0])
        return block_tag
    
    if blocktype == BlockType.QUOTE:
        block_tag = '<blockquote>'
        return block_tag
    
    if blocktype == BlockType.CODE:
        block_tag = '<code>'
        return block_tag

    if blocktype == BlockType.UNORDERED_LIST:
        block_tag = '<ul>'
        return block_tag

    if blocktype == BlockType.ORDERED_LIST:
        block_tag = '<ol>'
        return block_tag
    