#!/usr/bin/env python3.9


def calc2(data):
    # part 1 - do some calc
    SUM = 2020
    found = []
    for i in range(len(data)):
        for x in range(len(data)):
            #print(int(data[i]),int(data[x]), int(data[i])+int(data[x]))
            if (int(data[i]) + int(data[x])) == SUM:
                # find all possible solitions where SUM == 2020
                found.append([data[i], data[x]])

    # removing duplicates/double finds
    return list(set(x for l in found for x in l))


def calc3(data):
    # part 2 - do some calc
    data = sorted(data, key=lambda x: int(x))

    SUM = 2020
    found = []
    for x in range(len(data)):
        for y in range(len(data)):
            for z in range(len(data)):
                #print(int(data[x]),int(data[y]), int(data[z]), int(data[x])+int(data[y])+int(data[z]))
                if (int(data[x]) + int(data[y]) + int(data[z])) == SUM:
                    # find all possible solitions where SUM == 2020
                    found.append([data[x], data[y], data[z]])

                    # removing duplicates/double finds
                    # find only one solution(complexity)
                    return list(set(x for l in found for x in l))


with open("input.txt", "r") as file:
    input = file.read().splitlines()

    solution_part_1 = calc2(input)
    flag1 = int(solution_part_1[0]) * int(solution_part_1[1])
    print("###Solution Part 1 ###")
    print("Found pair: " + solution_part_1[0] +
          " + " + solution_part_1[1] + " = 2020")
    print("Flag is: " + str(flag1))

    solution_part_2 = calc3(input)
    flag2 = int(solution_part_2[0]) * \
        int(solution_part_2[1]) * int(solution_part_2[2])
    print("\n###Solution Part 2 ###")
    print("Found pair: " + solution_part_2[0] + " + " +
          solution_part_2[1] + " + " + solution_part_2[2] + " = 2020")
    print("Flag is: " + str(flag2))
