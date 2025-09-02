import argparse

from gendiff.engine import generate_diff, parsers


def main():

    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
        )
    
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')

    args = parser.parse_args()
    
    file1_data = parsers.read_json(args.first_file)
    file2_data = parsers.read_json(args.second_file)

    diff = generate_diff.generate_diff(file1_data, file2_data)

    print(diff)


if __name__ == "__main__":
    main()