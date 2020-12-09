#!/usr/bin/env python3.9


def sum_elements(elem):
    sum1 = 0
    for i in elem:
        sum1 += int(i)
    return sum1


def check_enc(data, result_p1):
    start = 0
    i = 0
    mysum = 0
    while int(mysum) != int(result_p1):
        if int(mysum) < int(result_p1):
            mysum = sum_elements(data[start:start+i])

        if int(mysum) > int(result_p1):
            start += 1
            i = 0
            mysum = 0

        if int(mysum) == int(result_p1):
            # print("FOUND: ",data[start:start+i])
            solution = data[start:start+i]
            solution_sorted = sorted(solution, key=lambda x: int(x))
            erg = int(solution_sorted[0])+int(solution_sorted[-1])
            return erg

        i += 1


def check_valid(data, range_preamble, start):

    preamble = data[start:start+range_preamble]
    target = data[len(data[:start+range_preamble])]

    # only test smaller than target
    preamble = sorted([i for i in preamble if int(i) < int(target)])

    for x in preamble:
        for y in preamble:
            if int(x)+int(y) == int(target):
                return x, y, target
    return 0


with open("input.txt", "r") as file:
    data = file.read().splitlines()

# print(data)
range_preamble = 25
start = 0

result_p1 = 0
for item in data:
    result = check_valid(data, range_preamble, start)
    if not result:
        result_p1 = data[start+range_preamble]
        print(result_p1)
        break
    start += 1

# part 2
print(check_enc(data, result_p1))
