    #
import pytest
from gendiff.engine import generate_diff, parsers

def load_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()

def test_generate_diff():
    file1_path = 'tests/test_data/file1.json'
    file2_path = 'tests/test_data/file2.json'
    expected_diff_path = 'tests/test_data/expected_diff.txt'

    data1 = parsers.load_data(file1_path)
    data2 = parsers.load_data(file2_path)
    expected_diff = load_file(expected_diff_path)

    actual_diff = generate_diff.generate_diff(data1, data2)

    assert actual_diff == expected_diff