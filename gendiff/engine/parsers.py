import json
import os

import yaml


def read_file(file_path):
    _, file_extension = os.path.splitext(file_path)
    if file_extension in ('.json'):
        with open(file_path, 'r') as f:
            data = json.load(f)
        return data
    elif file_extension in ('.yml', '.yaml'):
        with open(file_path, 'r') as f:
            data = yaml.safe_load(f)
        return data


def load_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()