import unittest
from blocktype import block_to_block_type, BlockType
from md_to_block import markdown_to_blocks

class TestTextTo(unittest.TestCase):
    def test_text_to_1(self):
        text = "```\nsome code\n\nmore code\n```"
        markdown = markdown_to_blocks(text)
        test_bt = block_to_block_type(markdown[0])
        self.assertIs(BlockType.CODE, test_bt)