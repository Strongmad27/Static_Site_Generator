import unittest
from blocktype import block_to_block_type, BlockType
from md_to_block import markdown_to_blocks

class TestTextTo(unittest.TestCase):
    def test_text_to_1(self):
        text = "```\nprint('hello')\n```"
        markdown = markdown_to_blocks(text)
        test_bt = block_to_block_type(markdown[0])
        self.assertIs(BlockType.CODE, test_bt)

    def test_text_to_2(self):
        text = "# ```\nprint('hello')\n```"
        markdown = markdown_to_blocks(text)
        test_bt = block_to_block_type(markdown[0])
        self.assertIs(BlockType.HEADING, test_bt)

    def test_text_to_3(self):
        text = "###### ```\nprint('hello')\n```"
        markdown = markdown_to_blocks(text)
        test_bt = block_to_block_type(markdown[0])
        self.assertIs(BlockType.HEADING, test_bt)

    def test_text_to_4(self):
        text = "> \n> ```\n>print('hello')\n>```"
        markdown = markdown_to_blocks(text)
        test_bt = block_to_block_type(markdown[0])
        self.assertIs(BlockType.QUOTE, test_bt)

    def test_text_to_5(self):
        text = "- \n- ```\n- print('hello')\n- ```"
        markdown = markdown_to_blocks(text)
        test_bt = block_to_block_type(markdown[0])
        self.assertIs(BlockType.UNORDERED_LIST, test_bt)

    def test_text_to_6(self):
        text = "1. \n2. ```\n3. print('hello')\n4. ```"
        markdown = markdown_to_blocks(text)
        test_bt = block_to_block_type(markdown[0])
        self.assertIs(BlockType.ORDERED_LIST, test_bt)

    def test_text_to_7(self):
        text = "1. \n2. ```\n3. print('hello')\n5. ```"
        markdown = markdown_to_blocks(text)
        test_bt = block_to_block_type(markdown[0])
        self.assertIsNot(BlockType.QUOTE, test_bt)