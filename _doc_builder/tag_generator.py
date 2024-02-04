#%%

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import nltk
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
