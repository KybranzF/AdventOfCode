#!/usr/bin/env python3.9

import time
import copy

def replaceX(db, coord, replacement):
    # print("DB   ", db)
    for i in range(len(db)):
        db[i] = list(db[i])
    # print(db)
    # replaceX(data, coord, "#")
    col = coord[0]
    # col = 1
    row = coord[1]
    # print("replace:",col,row,"with:" ,replacement)
    db[row][col] = replacement
    # print(db)
    # return db with replacement
    ret_db = []
    for i in db:
        ret_db.append("".join(i))
        # ret_db.append("".join(i))
    # print("RETDB",ret_db)
    # print()
    return ret_db

def check_adjacent(coord, data):
    col = coord[0]
    row = coord[1]
    # print("COL:",col,"ROW:",row)
    target = data[row][col]

    my_db = []

    above_l = ''
    above_m = ''
    above_r = ''
    left = ''
    right = ''
    below_l = ''
    below_m = ''
    below_r = ''

    # adjlogic
    # +++
    # ...
    # ...
    if row <= 0:
        above_l = "+"
        above_m = "+"
        above_r = "+"   
    
    # +..
    # +..
    # +..
    if col <= 0:
        above_l = "+"
        left = "+"
        below_l = "+"

    # ..+
    # ..+
    # ..+
    if col >= len(data[row])-1:
        above_r = "+"
        right = "+"
        below_r = "+"
    
    # ...
    # ...
    # +++
    if row >= len(data)-1:
        below_r = "+"
        below_m = "+"
        below_l = "+"

    if above_l != '+':
        above_l = data[row-1][col-1]
        my_db.append(above_l)

    if above_m != '+':
        above_m = data[row-1][col]
        my_db.append(above_m)

    if above_r != '+':
        above_r = data[row-1][col+1]
        my_db.append(above_r)

    if left != '+':
        left = data[row][col-1]
        my_db.append(left)

    if right != '+':
        right = data[row][col+1]
        my_db.append(right)

    if below_l != '+':
        below_l = data[row+1][col-1]
        my_db.append(below_l)

    if below_m != '+':
        below_m = data[row+1][col]
        my_db.append(below_m)

    if below_r != '+':
        below_r = data[row+1][col+1]
        my_db.append(below_r)

    l_counter = 0
    ht_counter = 0
    for i in my_db:
        if i == "L":
            l_counter += 1
        if i == "#":
            ht_counter += 1

    # print(above_l, above_m, above_r," ", "#: ", ht_counter)
    # print(left, "@", right," ", "L: ", l_counter)
    # print(below_l, below_m, below_r," ", "T: ", target)


        
    # return number of adjacent places filled/free
    return l_counter, ht_counter, target

with open("input1.txt", "r") as file:
    data = file.read().splitlines()
    data2 = copy.deepcopy(data)
    print(data2)
    # for i in range(len(data2)):
    #     data2[i] = list(data2[i])

    # for i in range(len(data)):
    #     data[i] = list(data[i])
    # print(data)
    data_tmp = copy.deepcopy(data)
    xxx = 0
    while xxx < 100:
        #rows : 98
        for x in range(len(data)):
            for y in range(len(data[x])):
                
                if x == 98:
                    print(data_tmp[x],data_tmp[y])

                coord = [x,y]
                l, ht, value = check_adjacent(coord,data2)
                # print(l, ht, value)
                if ht > 3 and value == "#":
                    # print("FOUND 4+: ",ht,coord)
                    # If a seat is occupied (#) and four or more seats adjacent to it are also occupied, 
                    # the seat becomes empty.
                    data_tmp = replaceX(data_tmp, coord, "L")

                if value == "L" and ht == 0:
                    # print("found empty seat with no # around: ",ht,coord)
                    # If a seat is empty (L) and there are no occupied seats adjacent to it,
                    data_tmp = replaceX(data_tmp, coord, "#") 
                    # the seat becomes occupied.
                if value == ".":
                    pass
      
        # time.sleep(0.5)
        xxx += 1

        data2 = copy.deepcopy(data_tmp)
        print()
        print("Round: ", xxx)
        for i in data_tmp:
            print("".join(i))
    print()
    print("FINAL")
    counterSeats = 0
    for i in data2:
        print("".join(i))
        for x in i:
            # print(x)
            if x == "#":
                counterSeats +=1
    # print(countAllHt(data))
    print("Seats available: ", counterSeats)
