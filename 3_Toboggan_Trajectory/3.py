#!/usr/bin/env python3.9


def calc(input, right, down):
    treecounter = 0
    way = 0
    for i in range(len(input)):
        col = list(input[i].replace("\n", ''))
        print("Round: ", i)
        # ignore round 0
        if i == 0:
            way = right
            continue
        # for multiple downs
        if down > 1:
            if i % down != 0:
                continue
        # calculate way
        while 1:
            if way < len(col):
                break
            else:
                way -= len(col)
        # count trees
        if col[way] == "#":
            print("found tree")
            treecounter += 1
        way += 31+right

    print("Trees" + str(right)+": "+str(down), treecounter)
    return treecounter


with open("input.txt", "r") as file:
    input = file.readlines()
    input = list(input)

    x1 = int(calc(input, 1, 1))
    x2 = int(calc(input, 3, 1))
    x3 = int(calc(input, 5, 1))
    x4 = int(calc(input, 7, 1))
    x5 = int(calc(input, 1, 2))

    print("FLAG: ", x1*x2*x3*x4*x5)
