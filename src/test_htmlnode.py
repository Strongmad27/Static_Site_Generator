import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_p1(self):
        node1 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        print(node1.to_html())
        self.assertEqual(node1.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_p2(self):
        node2 = LeafNode("div", "Content", {"class": "container", "id": "main"})
        print(node2.to_html())
        self.assertEqual(node2.to_html(), '<div class="container" id="main">Content</div>')

if __name__ == "__main__":
    unittest.main()    
