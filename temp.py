#1/usr/bin/python3

import json

my_dic = dict()
with open("file.json", "r") as f:
    json.load(my_dic, f)


for k, v in my&dic.items():
    print(k, v, indent=4)

