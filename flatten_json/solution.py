from itertools import chain, starmap


def flatten_data_recursive_solution(data, delimiter):
    flat_json = {}

    def flatten(x, name=''):
        if isinstance(x, dict):
            for key, value in x.items():
                flatten(value, name + key + delimiter)
        elif isinstance(x, list):
            i = 0
            for value in x:
                flatten(value, name + str(i) + delimiter)
                i += 1
        else:
            flat_json[name[:-1]] = x

    flatten(data)
    return flat_json


def flatten_data_iterative_solution(data, delimiter):

    def unpack_one_level(parent_key, parent_value):
        if isinstance(parent_value, dict):
            for key, value in parent_value.items():
                temp1 = parent_key + delimiter + key
                yield temp1, value
        elif isinstance(parent_value, list):
            i = 0
            for value in parent_value:
                temp2 = parent_key + delimiter + str(i)
                i += 1
                yield temp2, value
        else:
            yield parent_key, parent_value

    while True:
        data = dict(chain.from_iterable(starmap(unpack_one_level, data.items())))
        if not any(isinstance(value, dict) for value in data.values()) and \
                not any(isinstance(value, list) for value in data.values()):
            break

    return data
