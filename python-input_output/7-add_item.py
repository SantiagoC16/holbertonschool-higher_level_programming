#!/usr/bin/python3
"""task 7"""
from sys import argv
import os


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if os.path.exist("add_item.json"):

    list = load_from_json_file("add_item.json")
    for _read in range(1, len(argv)):
        list.append(argv[_read])
        save_to_json_file("add.item.json")
else:
    list = []
    for _read in range(1, len(argv)):
        list.append(argv[_read])
        save_to_json_file("add.item.json")
