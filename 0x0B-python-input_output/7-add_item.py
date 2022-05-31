#!/usr/bin/python3
"""
script that adds all arguments to a Python list,
and then save them to a file
"""


from sys import argv

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

file = "add_item.json"

try:
    list = load_from_json_file(file)
except FileNotFoundError:
    list = []
i = 1
if 0 < len(argv) is not 1:
    while i < len(argv):
        list.append(argv[i])
        i += 1
        
save_to_json_file(list, file)
