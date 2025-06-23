from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"
def block_to_block_type(markdown):
    md_copy = markdown.split("\n")
    if markdown.strip().startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if markdown[:3] == "```" and markdown[-3:] == "```":
        return BlockType.CODE
    for md in md_copy:
        if md[0] != ">":
            break
    else:
        return BlockType.QUOTE
    for md in md_copy:
        if md[:2] != "- ":
            break
    else:
        return BlockType.UNORDERED_LIST
    if markdown.strip().startswith("1. "):
        i = 1
        for line in md_copy:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH
    
    


    