from md_to_html_node import markdown_to_html_node
import os, shutil
from copy_static_public import copy_paste, public_clearing_house

def extract_title(markdown):
    lined_md = markdown.splitlines()
    for line in lined_md:
        if line.startswith('# '):
            return line[2:].strip()
    raise Exception ('no title header found')

def generate_page(from_path, template_path, dest_path):
    print(f'Generating page from {from_path} to {dest_path} using {template_path}')
    if not os.path.isfile(from_path):
        raise Exception ('from_path does not point to md file')
    with open(from_path) as source:
        read_source = source.read()
    with open(template_path) as template:
        read_template = template.read()
    if read_source == None:
        print ('read_source returning None')
    source_html = markdown_to_html_node(read_source).to_html()
    if source_html == None:
        print(f'\n\nsource_html returning None')
    source_title = extract_title(read_source)
    new_html = read_template.replace('{{ Title }}', source_title)
    new_html = new_html.replace('{{ Content }}', source_html)
    dest_dir = os.path.dirname(dest_path)
    os.makedirs(dest_dir, exist_ok=True)
    with open(dest_path, 'w') as file:
        file.write(new_html)
            
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    print(f'Generating pade from {dir_path_content} directory to Public')
    for item in os.listdir(dir_path_content):
        item_path = os.path.join(dir_path_content, item)
        pub_path = os.path.join(dest_dir_path, item)
        if os.path.isfile(item_path):
            if item_path.endswith('.md'):
                pub_path = pub_path.replace('.md', '.html')
                generate_page(item_path, template_path, pub_path)
            else:
                shutil.copy(item_path, pub_path)
            print(f'{pub_path}')
        elif os.path.isdir(item_path):
            public_clearing_house(pub_path)
            generate_pages_recursive(item_path, template_path, pub_path)
