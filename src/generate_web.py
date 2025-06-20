from md_to_html_node import markdown_to_html_node
import os

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
            

                
