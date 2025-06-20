import unittest
from md_to_html_node import markdown_to_html_node
from blocktype import block_to_block_type, BlockType
from md_to_block import markdown_to_blocks

class TestTextTo(unittest.TestCase):
    def test_ulist(self):
        md = """
- this
- is how *a* ulist
- should look
- B. Keller

and here is a paragraph
"""

        block = markdown_to_blocks(md)
        blocktype = block_to_block_type(block[0])
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
"<div><ul><li>this</li><li>is how <i>a</i> ulist</li><li>should look</li><li>B. Keller</li></ul><p>and here is a paragraph</p></div>",
)

