#!/usr/bin/env python3

"""Entrypoint."""

import json
import argparse
from flatten_json import flatteners


def parse_args() -> tuple[str, str, str, bool]:
    parser = argparse.ArgumentParser(prog = 'FlattenJSON',
                                     description = 'Convert Nested JSON Data to Flat JSON')
    parser.add_argument('filename', help='name json file')
    parser.add_argument('outfile', help='name output file')
    parser.add_argument('-d', '--delimiter', default='.')
    parser.add_argument('-r', '--recursive', action='store_true')
    args = parser.parse_args()

    return args.filename, args.outfile, args.delimiter, args.recursive


def read_file(filename: str) -> dict:
    with open(filename, 'r') as json_file:
        return json.load(json_file)

def write_file(data: dict, filename: str) -> None:
    with open(filename, 'w') as json_file:
        json.dump(data, json_file)


def main() -> None:
    """Main function."""

    filename, outfile, delimiter, recursive = parse_args()
    nested_json = read_file(filename)

    if recursive is True:
        flat_json = flatteners.flatten_data_recursive_solution(nested_json, delimiter)
    else:
        flat_json = flatteners.flatten_data_iterative_solution(nested_json, delimiter)

    write_file(flat_json, outfile)



if __name__ == '__main__':
    main()
