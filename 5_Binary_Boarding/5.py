#!/usr/bin/env python3.9

import math


def calc_seat_ID(row, col):
    seat_id = (row * 8) + col
    return seat_id


def logic(value, logic):
    # calculate current range
    ran = value[1]-value[0]+1

    # lower half
    if logic == 'F' or logic == 'L':
        value[1] = math.floor(value[1]-(ran/2))

    # upper half
    elif logic == 'B' or logic == 'R':
        value[0] = math.ceil(value[0]+((value[1]-value[0])/2))

    return value


def check(data):
    row_range = [0, 127]
    col_range = [0, 7]
    row = 0
    col = 0

    # row
    for item in data[:7]:
        row_range = logic(row_range, item)
        row = row_range[0]

    # col
    for item in data[7:]:
        col_range = logic(col_range, item)
        col = col_range[0]

    return [row, col]


with open("input.txt", "r") as file:
    lines = file.readlines()
    id_db = []
    for line in lines:
        # delete \n
        if len(line) == 11:
            line = line[:-1]

        result = check(line)
        seat_id = calc_seat_ID(result[0], result[1])
        id_db.append(seat_id)
        # print(line,result,seat_id)
    print("Max seat ID: " + str(max(id_db)))

    # part 2
    id_db = sorted(id_db, key=lambda x: int(x))
    # print(id_db)
    for i in range(len(id_db)-1):
        if id_db[i]+1 != id_db[i+1]:
            print("My seat: ", id_db[i]+1)
