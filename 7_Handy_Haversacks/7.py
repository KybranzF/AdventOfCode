#!/usr/bin/env python3.9


# def checkP2(db, bags):
#     search = {}
#     for bag in bags:
        
#         x = bag.strip().split(" ",1)
#         search[x[1]] = x[0]

#         for key, value in db.items():
#             for item in value:
#                 # print(item.strip().split(" ",1)[1], x[1])
#                 if x[1] == item.strip().split(" ",1)[1]:
#                     print("found dupe: ", x[0], x[1], value,key)

#     return search

with open("input.txt", "r") as file:
    lines = file.read()
    groups = lines.split("\n")

    db = []
    dict_db = {}
    for item in groups:
        # clean up unusable info
        if "." in item:
            item = item.replace(".","")
        if " bags" in item:
            item = item.replace("bags","")
        if " bag" in item:
            item = item.replace("bag","")

        tmp = item.split("contain")

        dict_db[tmp[0]] = tmp[1].split(",")
    
    # search for all shiny gold occurences
    bag_stack = []
    bag_stack_for_part_2 = []
    for key, value in dict_db.items():
        for item in value:
            if "shiny gold" in item:
                # print(key,value)
                bag_stack.append(key)
        # P2
        if "shiny gold" in key:
            for i in value:
                bag_stack_for_part_2.append(i)

    # check where the found bags can be contained
    for bag in bag_stack:
        for key, value in dict_db.items():
            for item in value:
                # print(bag,item)
                if bag.strip() in item.strip():
                    bag_stack.append(key)

    # len of the unique list of bags that
    # can contain bags that contain shiny gold
    print("P1: Bag colors that can eventually contain at least one shiny gold bag?: ",len(list(set(bag_stack))))
    # print(bag_stack_for_part_2)
    # print(checkP2(dict_db,bag_stack_for_part_2))
    