import json


def read_file(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)