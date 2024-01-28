#%%
import os
import pathlib
import re
from .config import IGNORE_DIRS, CATEGORY_NAME_MAP
from loguru import logger

#Get PROJECT DIR
__filename = os.path.abspath (__file__)
path = pathlib.Path(__filename)
PROJECT_DIR = path.parent.parent.parent.resolve()

def abs_path(*paths:str) -> str: 
    """ Return the absolute path by joining the paths with the projectDir variable.

    Returns:
        str: Abslute path of the file
    """
    return os.path.abspath(os.path.join(PROJECT_DIR, *paths))


def relative_path(path:str) -> str:
    """ Return relative path from the project directory.

    Args:
        path (str): Absolute path

    Returns:
        str: Relative path
    """
    return os.path.relpath(path, PROJECT_DIR)

def to_camel_case(text:str) -> str:
    """ Replace the spaces and the letters after them with the uppercase version of the letters.

    Args:
        text (str): Original text

    Returns:
        str: camel case text
    """
    text = re.sub(r"\s(.)", lambda match: match.group(1).upper(), text)
    return text

def read_file(path:str, encoding:str="utf8") -> str:
    """ Return the file content as a string

    Args:
        path (str): File path
        encoding (str, optional): Text encoding method. Defaults to "utf8".

    Returns:
        str: File content
    """
    logger.info(f'path {path}')
    with open(path, "r", encoding=encoding) as f:
        return f.read()

def get_title(path:str) -> str:
    """ Get the markdown h2 title.

    Args:
        path (str): File path

    Returns:
        str: Markdown h2 title
    """
    content = read_file(path, encoding="utf8")
    matched = re.search(r"##? (.+)", content)
    if not matched:
        return ""
    title = matched.group(1)
    title = re.sub(r"\[(.*?)\]", r"\1", title)
    return title

def get_dir_list(dir):
    filenames = os.listdir(dir)
    dir_list = [name for name in filenames if pathlib.Path(abs_path(name)).is_dir() and not (name.startswith('_') or name.startswith('.') or name in IGNORE_DIRS)]
    logger.info(f'IGNORE_DIRS {IGNORE_DIRS}')
    return dir_list

def scan_dir(path, nodeMap, parentPath, _parent = None, level=3):
    dir_path = abs_path(parentPath,path)
    # print('dir_path',dir_path)
    file_list =  os.listdir(dir_path)
    # print('file_list',file_list)
    children = []
    cur_node = nodeMap[dir_path] = {
        "name": path,
        "path": dir_path,
        "title": CATEGORY_NAME_MAP.get(path, to_camel_case(path)),
        "isDir": True,
        "intro": None,
        "isSymbolicLink": False,
        "level": level,
        "children": children,
        "parent": _parent,
    }
    cur_parent_node = {
        "name": path,
        "path": dir_path,
        "title": CATEGORY_NAME_MAP.get(path, to_camel_case(path)),
        "isDir": True,
        "intro": None,
        "isSymbolicLink": False,
        "level": level,
        "parent": _parent,
    }
    # print(nodeMap)
    for index, filename in enumerate(file_list):
        cur_path = abs_path(dir_path, filename)
        # print(cur_path)
        stats = pathlib.Path(cur_path)
        if os.path.islink(cur_path):
            children.append({
                "name": path,
                "path": cur_path,
                "title": "",
                "isDir": False,
                "isSymbolicLink": True,
                "intro": None,
                "level": level,
                "children": [],
                "parent": cur_parent_node,
            })
            continue
        if stats.is_file():
            if filename.lower() == "readme.md":
                cur_node["intro"] = read_file(cur_path, encoding="utf8")
                continue
            title = get_title(cur_path)
            children.append({
                "name": path,
                "path": cur_path,
                "title": title,
                "isDir": False,
                "intro": None,
                "isSymbolicLink": False,
                "level": level,
                "children": [],
                "parent": cur_parent_node,
            })
        elif stats.is_dir():
            subNode = scan_dir(filename, nodeMap, dir_path, cur_parent_node, level + 1)
            subNode["parent"] = cur_node
            children.append(subNode)
        else:
            # ignore
            pass
    cur_node["children"] = [n for n in children if n]
    return cur_node

def get_root_node():
    dir_list = get_dir_list(PROJECT_DIR)
    nodeMap = {}
    rootNode = [] 
    for path in dir_list:
        tempnode = scan_dir(path, nodeMap, PROJECT_DIR, None, 2) 
        rootNode.append(tempnode)
    return rootNode