import yaml
with open('_config.yml', 'r') as file:
    config = yaml.safe_load(file)
    exclude = config['exclude']
IGNORE_DIRS = [
    'database', 'node_modules', 'makefile-utils', 'assets'
]+exclude


CATEGORY_NAME_MAP = {
    'ml': 'Machine Learning',
    'ds': 'Data Science',
    'raspberry-pi': 'Raspberry Pi',
    'ai-tools': 'AI Tools',
    'prompt-engineering': 'Prompt Engineering',
    'ab-testing': 'AB Testing',
    
}

STOP_WORD_LIST = []
# ['coding', 'programming', 'software', 'technology', 'computer science', 'python', 'developer', 'code', 'software development', 'programming languages', 'software engineering', 'digital', 'tech','programming','science','engineering','internet','web','website','online', 'ai', 'artificial intelligence', 'data', 'learning', ]