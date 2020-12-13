#!/usr/bin/env python3.9

from toolz import reduce, last

with open("input.txt", "r") as file:
    time,busses = file.read().splitlines()
    time = int(time)
    bus = [i for i in busses.split(",") if i != "x"]
    smallest = 0
    smallest_item = 0

    for item in bus:
        tmp = int(item)
        while tmp <= time:
            tmp += int(item)
        if smallest == 0:
            smallest = tmp
            smallest_item = item
        if tmp < smallest:
            smallest = tmp
            smallest_item = item
    diff = smallest - time

    # print("TIME: ", time)
    # print("Smallest: ", smallest, smallest_item)
    # print("Time diff: ", smallest - time)
    print(int(smallest_item)*diff)

    db = []
    busp2 = enumerate([i for i in busses.split(",")], start=0)
    for index, busID in busp2:
        if busID != "x":
            db.append((index,int(busID)))

    # print(db)

    N = reduce(lambda a, b: a * b, map(last, db))

    # print(N)

    print(sum((m - r) * N//m * pow(N//m, -1, m) for r, m in db) % N)
