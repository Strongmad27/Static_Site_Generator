from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"
def block_to_block_type(markdown):
    md_copy = markdown.split("\n")
    if markdown[:2] == "# " or markdown[:3] == "## " or markdown[:4] == "### " or markdown[:5] == "#### " or markdown[:6] == "##### " or markdown[:7] == "###### ":
        return BlockType.HEADING
    if markdown[:3] == "```" and markdown[-3:] == "```":
        return BlockType.CODE
    if "" in md_copy:
        return BlockType.PARAGRAPH
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
    
    


    