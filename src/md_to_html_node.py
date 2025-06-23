from blocktype import block_to_block_type, BlockType
from htmlnode import ParentNode, LeafNode
from md_to_block import markdown_to_blocks
from text_to import text_to_textnodes, text_node_to_html_node

##takes full markdown document and returns single parent node containg everything split into leaf nodes

       

def markdown_to_html_node(markdown):
    blocked_markdown_list = markdown_to_blocks(markdown)

    ## created list of markdown blocks to iterate over, determine types, then convert to HTMLNodes
    html_nodes = []
    for block in blocked_markdown_list:
        if not block.strip():
            continue
        blocktype = block_to_block_type(block)
        ##referencing blocktype, create HTMLNode from the block
        if blocktype != BlockType.CODE:
            block_lines = block.splitlines()
            block_tag = blocktype_to_tag(blocktype, block_lines)
            if blocktype == BlockType.ORDERED_LIST:
                ol_list = []
                ol_nodes = []
                ol_leafs = []
                orderded_html_nodes = []
                for line in block_lines:
                    new_line = line[3:]
                    ol_list.append(new_line)
                for trimmed_line in ol_list:
                    ol_tn = text_to_textnodes(trimmed_line)
                    for node in ol_tn:
                        ol_nodes.append(node)
                for ord_tn in ol_nodes:
                    ol_hn = text_node_to_html_node(ord_tn)
                    ol_leafs.append(ol_hn)
                for leaf in ol_leafs:
                    leaf_l = [leaf]
                    leaf_line = ParentNode('li', leaf_l)
                    orderded_html_nodes.append(leaf_line)
                new_list_node = ParentNode(block_tag, orderded_html_nodes)
                html_nodes.append(new_list_node)
                continue
            b_l_list = []
            for line in block_lines:
                tn_list = text_to_textnodes(line)
                b_l_list.append(tn_list)
            leaf_list=[]
            for tn_line in b_l_list:
                html_line = []                
                for node in tn_line:
                    new_HN = text_node_to_html_node(node)
                    html_line.append(new_HN)
                leaf_list.append(html_line)
            if blocktype == BlockType.UNORDERED_LIST:
                ul_list = []
                ul_nodes = []
                for line in block_lines:
                    new_line = line[2:]
                    ul_list.append(new_line)
                for trimmed_line in ul_list:
                    ul_hn_lines = []                    
                    ul_tn = text_to_textnodes(trimmed_line)
                    for tn in ul_tn:
                        ul_hn = text_node_to_html_node(tn)
                        ul_hn_lines.append(ul_hn)
                    leaf_line = ParentNode('li', ul_hn_lines)
                    ul_nodes.append(leaf_line)
                new_list_node = ParentNode(block_tag, ul_nodes)
                html_nodes.append(new_list_node)
                continue
            new_list=[]                
            if blocktype == BlockType.QUOTE:
                for line in block_lines:
                    new_line = line[2:]
                    new_list.append(new_line)
                delim = '\n'
                old_block = delim.join(new_list)
                new_html = raw_block_to_child_node(old_block, block_tag)
                html_nodes.append(new_html)
                continue
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
                continue
            if blocktype == BlockType.PARAGRAPH:
                new_html = raw_block_to_child_node(block, block_tag)
                html_nodes.append(new_html)
                continue
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
            continue
    big_bad_parent = ParentNode('div', html_nodes)
    return big_bad_parent

##helper functions below:

def raw_block_to_child_node(block, block_tag):
    hn_list = []
    if block_tag == 'p':
        spl_bl=block.split('\n')
        cleaned_text = []
        for line in spl_bl:
            stp_ln=line.strip()
            cleaned_text.append(stp_ln)
        spacer = ' '
        new_bl=spacer.join(cleaned_text)
        new_tn = text_to_textnodes(new_bl)
    else:
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
    parts = block.split(' ', 1)  # Split on first space only
    if len(parts) < 2:
        return None
    hash_part = parts[0]
    if hash_part and all(c == '#' for c in hash_part) and 1 <= len(hash_part) <= 6:
        return f'h{len(hash_part)}'
    return None

def blocktype_to_tag(blocktype, block_lines):
    if blocktype == BlockType.PARAGRAPH:
        block_tag = 'p'
        return block_tag
   
    if blocktype == BlockType.HEADING:
        block_tag = hash_counter(block_lines[0])
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
   


