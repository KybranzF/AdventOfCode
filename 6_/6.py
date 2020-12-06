#!/usr/bin/env python3.9

from collections import Counter


def find_yes(item):
    length = len(item)
    x = Counter(x for sublist in item for x in sublist)
    values = dict(x)
    yes_count = 0

    for key, value in values.items():
        if value == length:
            yes_count += 1

    return yes_count


with open("input.txt", "r") as file:
    lines = file.read()
    groups = lines.split("\n\n")
    yes_count = 0

    for i in groups:
        groups_tmp = i.replace("\n", "")
        unique = set(groups_tmp)
        yes_count += len(unique)

    print("Amount of group yes: ", yes_count)

    # Part 2
    result = 0
    for i in groups:
        groups_tmp = i.split("\n")
        result += find_yes(groups_tmp)

    print("Amount of yes in same group: ", result)
