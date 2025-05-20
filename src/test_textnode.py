import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_e2(self):
        node = TextNode("This is a text", TextType.ITALIC)
        node2 = TextNode("This is a text", TextType.ITALIC)
        self.assertEqual(node, node2)

    def test_e3(self):
        node = TextNode("This is a text node", TextType.BOLD, "www.google.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "www.google.com")
        self.assertEqual(node, node2)

    def test_e4(self):
        node = TextNode("This is a text", TextType.BOLD)
        node2 = TextNode("This is a text bold", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_e5(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()