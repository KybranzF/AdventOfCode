#!/usr/bin/env python3.9

# FILTER RULES
# 1-3 a: abcde 		at least 1 a at most 3 a
# 1-3 b: cdefg		at least 1 b at most 3 b
# 2-9 c: ccccccccc 	at least 2 c at most 9 c


def rulePart1(minCount, maxCount, character, password):
    # smaller than min -> wrong
    if password.count(character) < int(minCount):
        return 0
    # bigger than max -> wrong
    if password.count(character) > int(maxCount):
        return 0
    return password


def rulePart2(minCount, maxCount, character, password):
    # check if first occurrence has a valid index
    if password[int(minCount)-1] == character:
        # check if second is also valid -> wrong
        if password[int(maxCount)-1] == character:
            return 0
        return password

    # check if second occurrence has a valid index
    if password[int(maxCount)-1] == character:
        # check if second is also valid -> wrong
        if password[int(minCount)-1] == character:
            return 0
        return password


def test(data):
    minCount = data[0]
    maxCount = data[1]
    character = data[2]
    password = data[3]

    # if not rulePart1(minCount,maxCount, character, password):
    # return 0
    if not rulePart2(minCount, maxCount, character, password):
        return 0
    return 1


with open("input.txt", "r") as file:
    input = file.read().splitlines()
    count = 0
    for entries in input:
        # parsing string
        entries = entries.replace("-", " ")
        entries = entries.replace(":", "")
        entries = entries.split(" ")
        if test(entries):
            count += 1

    print("Found Tuples: ", count)
