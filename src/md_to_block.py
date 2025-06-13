def markdown_to_blocks(markdown):
    md_list = markdown.split('\n\n')
    node_list=[]
    for index, value in enumerate(md_list):
        if value != "" or value != '\n' or value != ' ':
            new_text = value.strip()
            node_list.append(new_text)
    return node_list

