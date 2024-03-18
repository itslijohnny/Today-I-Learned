from helper.lib import PROJECT_DIR,get_dir_list,scan_dir,abs_path,get_root_node,relative_path
import yaml
from loguru import logger

def genereate_toc(nodes, level_std, _structure,_toc): 
    for node in nodes:
        if node['level'] != level_std:
            continue

        level, children = node['level'], node['children']
        dir_nodes = []
        for child_node in children:
            if child_node['isDir']:
                dir_nodes.append(child_node)
        _toc.append({'name': node['title'], 'level': level})
        if len(dir_nodes)>0:
            genereate_toc(dir_nodes, level_std + 1, _structure,_toc)
    return _toc



def process_anchor_link(link_name):
    # return link_name.lower().replace(" ",'-')
    return link_name.replace(' ','%20')

def genereate_note_list(nodes, level_std, _structure): 
    for node in nodes:
        logger.info('loop start {} {}'.format(node['name'],str(level_std)))
        if node['level'] != level_std:
            continue

        level, intro, children = node['level'], node.get('intro', ''), node['children']
        file_nodes = []
        dir_nodes = []

        for child_node in children:
            if child_node['isDir']:
                dir_nodes.append(child_node)
            else:
                if child_node['isSymbolicLink']:
                    continue
                file_nodes.append(child_node)
        
        _level = '##'*(level-1)
        _structure.append(f'{_level} {node["title"]}')
        if intro:
            _structure.append(intro.strip() + '\n')

        for n in file_nodes:
            # print('n',f'- [{n["title"]}]({process_anchor_link(relative_path(n["path"]))})  ')
            if n["title"] != '':
                _structure.append(f'- [{n["title"]}]({process_anchor_link(relative_path(n["path"]))})')
        if len(dir_nodes)>0:
            # print('dir_nodes',dir_nodes)
            genereate_note_list(dir_nodes, level_std + 1, _structure)
            continue
        _structure.append('\n\n[`⬆ Back to TOC`](#toc)')
    return _structure

def main():
    rootNode = get_root_node()
    with open(abs_path('_config.yml'), 'r') as file:
        config = yaml.safe_load(file)
    title = config['title']
    description = config['tagline']
    structure = [
        f'## {title}\n',
        f'> {description}\n',
        ]
    for file in ['_docs/intro.md','_docs/issue.md']:
        with open(abs_path(file), 'r') as f:
            content =  f.read() 
        structure.append(content)
    structure.append('\n------\n## TOC\n<!-- toc -->\n<!-- <details close> -->\n<!-- <summary>Collapse/Expand</summary> -->')
    toc = genereate_toc(rootNode, 2, structure,[])
    for t in toc:
        toc_level = '  '*(t['level']-2)
        structure.append(f'{toc_level}- [{t["name"]}](#{process_anchor_link(t["name"])})') 
    structure.append('\n<!-- </details> -->\n<!-- tocstop -->\n------') 
    structure = genereate_note_list(rootNode, 2, structure)
    with open(abs_path('README.md'), 'w') as f: 
        f.write('\n'.join(structure))

main()
