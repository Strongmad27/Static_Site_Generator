from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"
def block_to_block_type(md):
    md_copy = md.split("\n")
    if md[:2] == "# " or md[:3] == "## " or md[:4] == "### " or md[:5] == "#### " or md[:6] == "##### " or md[:7] == "###### ":
        return BlockType.HEADING
    if md[:3] == "```" and md[-3:] == "```":
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
    for i in range(0, len(md_copy)):
        x = i + 1
        prefix = str(f'{x}. ')
        if not md_copy[i].startswith(prefix):
            break
    else:
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH
    
    


    