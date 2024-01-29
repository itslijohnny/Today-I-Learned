import yaml
with open('_config.yml', 'r') as file:
    config = yaml.safe_load(file)
    exclude = config['exclude']
IGNORE_DIRS = [
    'database', 'node_modules', 'makefile-utils'
]+exclude


CATEGORY_NAME_MAP = {
    'ml': 'Machine Learning',
    'raspberry-pi': 'Raspberry Pi',
    'docker': 'Docker',
    'python': 'Python'
}