from textnode import TextNode, TextType
from htmlnode import HTMLNode, ParentNode, LeafNode

def main():
    node = TextNode("bla bla bla", TextType.BOLD)

    print(node)

def text_node_to_html_node(text_node):
    if isinstance(text_node, TextNode):
        if text_node.text_type == TextType.TEXT:
            return LeafNode(None, text_node.text)
        if text_node.text_type == TextType.BOLD:
            return LeafNode("b", text_node.text)
        if text_node.text_type == TextType.ITALIC:
            return LeafNode("i", text_node.text)
        if text_node.text_type == TextType.CODE:
            return LeafNode("code", text_node.text)
        if text_node.text_type == TextType.LINK:
            return LeafNode("a", text_node.text, {'href': text_node.url})
        if text_node.text_type == TextType.IMAGE:
            return LeafNode("img", "", {"alt": text_node.text,
                                          "src": text_node.url
                                          } )
    raise Exception ("Text Type not found in class ENUM")    

if __name__ == "__main__":
    main()