
import json
import yaml
from pprint import pprint as pp

with open("file.json") as f:
    json_lst = json.load(f)

with open("file.yml") as g:
    yml_lst = yaml.load(g)

pp(json_lst)
pp(yml_lst)
