#%%
from helper.lib import PROJECT_DIR,get_dir_list,scan_dir,abs_path,get_root_node,relative_path
import yaml
from loguru import logger
import os
import sys, getopt

# %%
def update_file_title_and_name(nodes, level_std,is_deploy): 
    for node in nodes:
        if node['level'] != level_std:
            continue
        level, children = node['level'], node['children']
        dir_nodes = []
        for child_node in children:
            if child_node['isDir']:
                dir_nodes.append(child_node)
            elif not child_node['isSymbolicLink'] and not child_node['isDir']:
                if child_node['title'] == '' or " " in child_node['path']:
                    generate_title_from_path(child_node['path'])
                    if is_deploy:
                        rename_file(child_node['path'])
                    logger.info('Name Updated {}'.format(child_node['path']))
        if len(dir_nodes)>0:
            update_file_title_and_name(dir_nodes, level_std + 1,is_deploy)

def generate_title_from_path(path):
    title = path.split('/')[-1].replace('.md','')
    logger.info(title)
    #insert title into file
    with open(path, 'r+') as f:
        content = f.read()
        if f'# {title}\n\n' in content:
            return
        f.seek(0)
        f.write(f'# {title}\n\n{content}')

def rename_file(path):
    base_dir = os.path.dirname(path)
    new_name = path.split('/')[-1].replace('.md','')
    new_name = '-'.join(e.lower() for e in new_name.split(' ') if e.isalnum())
    new_name = new_name + '.md'
    new_path = os.path.join(base_dir, new_name)
    os.rename(path, new_path)

# %%
def main(argv):
    is_deploy = False
    if argv:
        if argv[0] == 'deploy':
            is_deploy = True
            logger.info('Deploy mode is on')
    rootNode = get_root_node()
    logger.info(rootNode)
    update_file_title_and_name(rootNode, 2, is_deploy)

main(sys.argv[1:])
