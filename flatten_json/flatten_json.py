#!/usr/bin/env python3

"""Entrypoint."""

import json
import argparse
from flatten_json import solution


def create_parser():
    parser = argparse.ArgumentParser(prog = 'FlattenJSON',
                                     description = 'Convert Nested JSON Data to Flat JSON')
    parser.add_argument('filename', help='name json file')
    parser.add_argument('outfile', help='name output file')
    parser.add_argument('-d', '--delimiter', default='.')
    parser.add_argument('-r', '--recursive', action='store_true')

    return parser.parse_args()


def read_file(filename):
    with open(filename, 'r') as json_file:
        return json.load(json_file)

def write_file(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file)


def main() -> None:
    """Main function."""

    parser = create_parser()
    nested_json = read_file(parser.filename)

    if parser.recursive is True:
        flat_json = solution.flatten_data_recursive_solution(nested_json, parser.delimiter)
    else:
        flat_json = solution.flatten_data_iterative_solution(nested_json, parser.delimiter)

    write_file(flat_json, parser.outfile)



if __name__ == '__main__':
    main()
