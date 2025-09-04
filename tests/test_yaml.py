from gendiff.engine import generate_diff, parsers




def test_generate_diff():
    file1_path = 'tests/test_data/file1.yml'
    file2_path = 'tests/test_data/file2.yml'
    expected_diff_path = 'tests/test_data/result_yml.txt'

    data1 = parsers.read_file(file1_path)
    data2 = parsers.read_file(file2_path)
    expected_diff = parsers.load_file(expected_diff_path)

    actual_diff = generate_diff.generate_diff(data1, data2)

    assert actual_diff == expected_diff