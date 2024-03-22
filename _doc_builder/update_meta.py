from helper.lib import PROJECT_DIR,get_dir_list,scan_dir,abs_path,get_root_node
from tag_generator import get_tags,get_tag_from_meta
import os

def create_index_file_for_folder(node):
    index_filepath = os.path.join(node['path'], 'index.md')

    try:
        with open(os.path.join(node['path'], 'README.md'), 'r') as f:
            content = f.read()
    except OSError:
        content = ''

    node_title = node['title']
    node_parent_title = 'parent: '+node['parent']['title'] if node['parent'] else '' 

    with open(index_filepath, 'w') as f:
        f.write(f'---\nlayout: default\ntitle: {node_title}\nhas_children: true\n{node_parent_title}\n---\n\n{content}')
    print(f'Wrote: {index_filepath}')

    
def convert_symlink(symlink_path,meta_info):
    # Get the path of the referenced file
    target_path = os.readlink(symlink_path)

    # Open the referenced file and read its contents
    with open(target_path, 'r') as f:
        content = f.read()

    # Create a new file with the same name as the symlink
    # new_file_path = os.path.join(os.path.dirname(symlink_path), os.path.basename(symlink_path))
    # if os.path.exists(symlink_path):
    os.remove(symlink_path)

    with open(symlink_path, 'w') as f:
        f.write('\n'.join(meta_info))
        f.write(content)

    print(f"Created file {symlink_path} with the content of {target_path}")

def generate_meta_info(node, hide=False):
    datetime = node["date_time"]
    meta_raw = [
            '---',
            'layout: default',
            f'last_modified_date: {datetime}',
        ]
    if hide:
        meta_raw.append('nav_exclude: true')
    if node['parent']:
        node_parent_title = node['parent']['title']
        meta_raw.append(f'parent: {node_parent_title}')
        if node['parent']['parent']:
            node_gp_title = node['parent']['parent']['title']
            meta_raw.append(f'grand_parent: {node_gp_title}') 
    with open(node['path'], 'r') as f:
        content = f.read()
    des_tags = (" ").join(get_tags(content))
    tags = ("\n - ").join(get_tag_from_meta(content))
    meta_raw.append(f'tags: {tags}')
    meta_raw.append(f'description: {des_tags}')
    meta_raw.extend(['---', '', ''])
    return meta_raw 

def handle_symlinks(nodes,symlink_map):
    for node in nodes:
        if node['isDir']:
            handle_symlinks(node['children'], symlink_map)
        if not node['isSymbolicLink']:
            continue
        print(node)
        symlink_map[node['path']] = True 
        meta_raw = generate_meta_info(node,True)
        convert_symlink(node['path'],meta_raw) 


def process(nodes, symlink_map):
    for node in nodes:
        if node['isDir']:
            create_index_file_for_folder(node)
            process(node['children'],symlink_map)
            continue
        if node['path'] in symlink_map.keys():
            continue
        meta_raw = generate_meta_info(node)
        with open(node['path'], 'r+') as fh:
            buffer = fh.read()
            buffer = buffer.replace('.md)', '.html)')
            if '---\nlayout: default' in buffer:
                print(f"YAML front matter already exists in {node['path']}")
                continue
            fh.seek(0)
            fh.write('\n'.join(meta_raw))
            fh.write(buffer)

        print(f"Added YAML front: {node['path']}")


def update_readme():
    with open(abs_path('README.md'), 'r+') as fh:
        meta_raw = '---\ntitle: Home\nnav_order: 1\n---\n'
        buffer = fh.read()
        if '---\nlayout: default' in buffer:
            print(f"YAML front matter already exists in {abs_path('README.md')}")
            return
        fh.seek(0)
        fh.write(meta_raw + buffer)


def main():
    rootNode = get_root_node()
    symlink_map = {}
    handle_symlinks(rootNode,symlink_map) 
    process(rootNode,symlink_map)
    update_readme()
main()

