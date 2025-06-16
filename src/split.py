from textnode import TextType, TextNode
from extract import extract_markdown_images, extract_markdown_links

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        node_text = node.text
        node_texttype = node.text_type
        split_node = node_text.split(delimiter)
        if node_texttype != TextType.TEXT:
            new_nodes.append(node)
            continue
        elif len(split_node) % 2 == 0:
            raise Exception ("delimiter not found")
        else:
            for index, words in enumerate(split_node):            
                if words == "":
                    continue
                if index % 2 != 0:
                    new_TextNode = TextNode(words, text_type)
                    new_nodes.append(new_TextNode)
                else:
                    new_TextNode = TextNode(words, TextType.TEXT)
                    new_nodes.append(new_TextNode)
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        current_text = node.text
        node_texttype = node.text_type
        if node_texttype != TextType.TEXT:
            new_nodes.append(node)
            continue
        while True:
            check_tup = extract_markdown_images(current_text)
            if not check_tup and current_text != "":
                new_textnode = TextNode(current_text, TextType.TEXT)
                new_nodes.append(new_textnode)
                break
            elif not check_tup:
                break
            alt_text = check_tup[0][0]
            image_url = check_tup[0][1]
            image_str = f'![{alt_text}]({image_url})'
            split_text = current_text.split(f'{image_str}', 1)
            if split_text[0]:
                new_text = split_text[0]
                new_textnode = TextNode(new_text, TextType.TEXT)
                new_nodes.append(new_textnode)
            new_imagenode = TextNode(alt_text, TextType.IMAGE, image_url)
            new_nodes.append(new_imagenode)
            current_text = str(split_text[1])
    return new_nodes            

def split_nodes_links(old_nodes):
    new_nodes = []
    for node in old_nodes:
        current_text = node.text
        node_texttype = node.text_type
        if node_texttype != TextType.TEXT:
            new_nodes.append(node)
            continue
        while True:
            check_tup = extract_markdown_links(current_text)
            if not check_tup and current_text != "":
                new_textnode = TextNode(current_text, TextType.TEXT)
                new_nodes.append(new_textnode)
                break
            elif not check_tup:
                break
            alt_text = check_tup[0][0]
            link_url = check_tup[0][1]
            link_str = f'[{alt_text}]({link_url})'
            split_text = current_text.split(f'{link_str}', 1)
            if split_text[0]:
                new_text = split_text[0]
                new_textnode = TextNode(new_text, TextType.TEXT)
                new_nodes.append(new_textnode)
            new_linknode = TextNode(alt_text, TextType.LINK, link_url)
            new_nodes.append(new_linknode)
            current_text = str(split_text[1])
    return new_nodes       

           