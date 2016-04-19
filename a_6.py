

import yaml
import json

my_lst = [0,1,2,3,4,5,6,7,8,9, 'Ok', 'Not_Ok', {'key_1': [0,1,2,3,4,5], 'key_2': [6,7,8,9,]}]

print yaml.dump(my_lst, default_flow_style=False)

with open("file.yml", "w") as f:
    f.write(yaml.dump(my_lst, default_flow_style=False))

with open("file.json", "w") as g:
    json.dump(my_lst, g)

