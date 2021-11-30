import json

from typing import Dict

with open('01.json') as f:
    initial_data = json.load(f)


# initial_data = json.loads('[1,"red",5]')


def flatten_sum(data, num=0):
    match data:
        case dict():
            num += flatten_sum(data.keys())
            num += flatten_sum(list(data.values()))
        case list():
            for x in data:
                num += flatten_sum(x)
        case int():
            num += data
    return num


def flatten_sum_without_red(data, num=0):
    match data:
        case dict():
            if 'red' in data or 'red' in data.values():
                return 0
            num += flatten_sum_without_red(data.keys())
            num += flatten_sum_without_red(list(data.values()))
        case list():
            for x in data:
                num += flatten_sum_without_red(x)
        case int():
            num += data
    return num


print("Part 1:", flatten_sum(initial_data))
print("Part 2:", flatten_sum_without_red(initial_data))
