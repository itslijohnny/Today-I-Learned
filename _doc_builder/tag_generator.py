#%%

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import nltk
import re
nltk.download('punkt') # Download the Punkt tokenizer for sentence splitting
tokenizer = AutoTokenizer.from_pretrained("fabiochiu/t5-base-tag-generation")
model = AutoModelForSeq2SeqLM.from_pretrained("fabiochiu/t5-base-tag-generation")
from helper.config import STOP_WORD_LIST

# from helper.lib import PROJECT_DIR,get_dir_list,scan_dir,abs_path,get_root_node
#%%

def get_tags(text):
    inputs = tokenizer([text], max_length=512, truncation=True, return_tensors="pt")
    output = model.generate(**inputs, num_beams=8, do_sample=True, min_length=10,max_length=256)
    decoded_output = tokenizer.batch_decode(output, skip_special_tokens=True)[0]
    tags = list(set(decoded_output.strip().split(", ")))
    return [t for t in tags if t.lower() not in STOP_WORD_LIST]

def get_tag_from_meta(content):
    front_matter = re.search(r'---(.*?)---', content, re.DOTALL)
    if front_matter:
        # Extract the tags section
        content = content.replace("\n","\n ")
        tags_section = re.search(r'tags:(.*?)(\n[a-z]+:|$)', content, re.DOTALL)
        print(tags_section)
        if tags_section:
            # Extract the individual tags
            tags = re.findall(r'- (.*?)\n', tags_section.group(1))
            return [tag.strip() for tag in tags if tag]
    return []

#%%    
# def process(nodes, symlink_map):
#     for node in nodes:
#         if node['isDir']:
#             process(node['children'],symlink_map)
#             continue
#         if node['path'] in symlink_map.keys():
#             continue
#         with open(node['path'], 'r+') as fh:
#             text = fh.read()
            
#         print(get_tags(text))
# #%%
# process(get_root_node(),{})


# %%
