import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        tst_props = {
    "href": "https://www.google.com",
    "target": "_blank",
}
        html_str = ' href="https://www.google.com" target="_blank"'
        tst = HTMLNode(tag = 'a', props = tst_props)
        self.assertEqual(tst.props_to_html(), html_str)

    def test_eq2(self):
        tst_props = {}
        html_str = ''
        tst = HTMLNode(tag = 'a', props = tst_props)
        self.assertEqual(tst.props_to_html(), html_str)

    def test_eq3(self):
        tst_props = None
        html_str = ""
        tst = HTMLNode(tag = 'a', props = tst_props)
        self.assertEqual(tst.props_to_html(), html_str)



if __name__ == "__main__":
    unittest.main()    
