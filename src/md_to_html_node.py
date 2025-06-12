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
            block_lines = block.splitlines()
            b_l_list = []
            for line in block_lines:
                tn_list = text_to_textnodes(line)
                b_l_list.append(tn_list)
                ###creates a matrix of lists of textnodes, where each inner list of textnodes representing an entire line of the block
            leaf_list=[]
            for tn_line in b_l_list:
                html_line = []                
                for node in tn_line:
                    new_HN = text_node_to_html_node(node)
                    html_line.append(new_HN)
                leaf_list.append(html_line)
            block_tag = blocktype_to_tag(blocktype, block)
            if blocktype == BlockType.UNORDERED_LIST or blocktype == BlockType.ORDERED_LIST:
                new_list_node = list_block_to_HTMLNode(leaf_list, block_tag)
                html_nodes.append(new_list_node)
            new_list=[]
            if blocktype == BlockType.QUOTE:
                for line in block_lines:
                    new_line = line[1:]
                    new_list.append(new_line)
                delim = '\n'
                old_block = delim.join(block_lines)
                new_html = raw_block_to_child_node(old_block, block_tag)
                html_nodes.append(new_html)
            if blocktype == BlockType.HEADING:
                fir_str = block_lines[0]
                if block_tag == 'h1':
                    fir_str = fir_str[2:]
                elif block_tag == 'h2':
                    fir_str = fir_str[3:]
                elif block_tag == 'h3':
                    fir_str = fir_str[4:]
                elif block_tag == 'h4':
                    fir_str = fir_str[5:]
                elif block_tag == 'h5':
                    fir_str = fir_str[6:]
                elif block_tag == 'h6':
                    fir_str = fir_str[7:]
                block_lines[0] = fir_str
                delim = '\n'
                old_block = delim.join(block_lines)
                new_html = raw_block_to_child_node(old_block, block_tag)
                html_nodes.append(new_html)
            if blocktype == BlockType.PARAGRAPH:
                new_html = raw_block_to_child_node(block, block_tag)
                html_nodes.append(new_html)
        if blocktype == BlockType.CODE:
            code_text_list = block.splitlines()
            code_text_list = code_text_list[1:-1]
            text_list=[]
            for line in code_text_list:
                st_line = line.strip()
                text_list.append(st_line)
            new_line = '\n'
            code_text = new_line.join(text_list)+'\n'
            new_leaf = [LeafNode(None, code_text),]
            co_leafs = [ParentNode('code', new_leaf)]
            new_code_par = ParentNode('pre', co_leafs)
            html_nodes.append(new_code_par)
    big_bad_parent = ParentNode('div', html_nodes)
    return big_bad_parent

##helper functions below:

def raw_block_to_child_node(block, block_tag):
    hn_list = []
    new_tn = text_to_textnodes(block)
    for tn in new_tn:
        new_leaf = text_node_to_html_node(tn)
        hn_list.append(new_leaf)
    new_par = ParentNode(block_tag, hn_list)
    return new_par


def list_block_to_HTMLNode(leaf_list, block_tag):
    leafs = []
    for leaf in leaf_list:
        leaf_line = ParentNode('li', leaf)
        leafs.append(leaf_line)
    new_list_node = ParentNode(block_tag, leafs)
    return new_list_node

def hash_counter(block):
    hash = '#'
    i = 0
    length = max(7, len(block))
    for i in range(0, length):
        if block[i] == hash:
            i += 1
        elif block[i] == ' ':
            return f'h{i}'

def blocktype_to_tag(blocktype, block):
    if blocktype == BlockType.PARAGRAPH:
        block_tag = 'p'
        return block_tag
   
    if blocktype == BlockType.HEADING:
        block_tag = hash_counter(block[0])
        return block_tag
   
    if blocktype == BlockType.QUOTE:
        block_tag = 'blockquote'
        return block_tag
   
    if blocktype == BlockType.CODE:
        block_tag = 'code'
        return block_tag

    if blocktype == BlockType.UNORDERED_LIST:
        block_tag = 'ul'
        return block_tag

    if blocktype == BlockType.ORDERED_LIST:
        block_tag = 'ol'
        return block_tag
   


