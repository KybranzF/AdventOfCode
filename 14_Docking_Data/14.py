#!/usr/bin/env python3.9


def calcBin(value):
    binary = '{0:036b}'.format(value)
    return binary

with open("input.txt", "r") as file:
    db = []
    tmp = []
    
    for line in file:
        tmp.append(line.strip().replace(" ","").split("="))
        if "mask" in line:
            db.append(tmp)
            tmp = []
    # print(db)

    [[print(calcBin(int(i[1]))) for i in db[gogo] if "mask" not in i] for gogo in range(len(db))]

