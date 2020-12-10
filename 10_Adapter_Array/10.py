#!/usr/bin/env python3.9


def countALL(result, numbers):
    # this func: stolen from
    # https://www.reddit.com/r/adventofcode/comments/ka8z8x/2020_day_10_solutions/gf9zvav/?context=3
    numbers = list(map(int, numbers))
    a2, x = 1, 0
    l = []
    while x < len(numbers):

        if numbers[x] + 1 in numbers:
            l.append(numbers[x])
        elif numbers[x] + 1 not in numbers:
            if len(l) > 1:
                #    x * 8 - 1
                a2 = a2 * (pow(2, len(l) - 1) - max((len(l) - 3), 0))
            l = []
        x += 1
    return(a2)


def myMax(L):
    answer = 0
    for i in L:
        if int(i) > int(answer):
            answer = i
    return answer


def check_distance_to_next(index, data):
    if index < len(data):
        a = int(data[index+1])
        b = int(data[index])
        return a - b
    else:
        return 0


with open("input.txt", "r") as file:
    data = file.read().splitlines()

    # add starting point:
    data.append(0)

    # add our own adapter:
    myadapter = int(myMax(data)) + 3
    data.append(myadapter)

    # sort the string data to int
    sort = sorted(data, key=lambda x: int(x))

    db = []
    for item in range(len(sort)-1):
        result = check_distance_to_next(int(item), sort)
        if result:
            db.append(result)

    print((db.count(1))*(db.count(3)))

    print(countALL(db, sort))
