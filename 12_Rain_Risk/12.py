#!/usr/bin/env python3.9
import copy
from itertools import cycle, islice


def shift(d, n):
    return dict(zip(d, islice(cycle(d.values()), n, None)))


def rotateWaypoint(waypoint, operation):
    tmp_waypoint = copy.deepcopy(waypoint)

    o_direction = operation[:1]
    o_value = int(operation[1:])

    if o_direction == "R":
        # +
        if o_value == 90:
            tmp_waypoint = shift(waypoint, 3)
        elif o_value == 180:
            tmp_waypoint = shift(waypoint, 2)
        elif o_value == 270:
            tmp_waypoint = shift(waypoint, 1)
        elif o_value == 360:
            tmp_waypoint = shift(waypoint, 4)
        else:
            print("error")
            exit()

    elif o_direction == "L":
        # -
        if o_value == 90:
            tmp_waypoint = shift(waypoint, 1)
        elif o_value == 180:
            tmp_waypoint = shift(waypoint, 2)
        elif o_value == 270:
            tmp_waypoint = shift(waypoint, 3)
        elif o_value == 360:
            tmp_waypoint = shift(waypoint, 4)
        else:
            print("error")
            exit()
    return tmp_waypoint


def findDirection(current_facing, operation):
    o_direction = operation[:1]
    o_value = int(operation[1:])

    current_facing_degree = 0
    if current_facing == "N":
        pass
    if current_facing == "E":
        current_facing_degree = 90
    if current_facing == "S":
        current_facing_degree = 180
    if current_facing == "W":
        current_facing_degree = 270

    degree = 0
    if o_direction == "R":
        # +
        degree = current_facing_degree + o_value
    elif o_direction == "L":
        # -
        degree = current_facing_degree - o_value

    # shrink to 360 degree
    if degree > 360:
        # print(degree)
        degree = abs(360 - degree)

    # calculate new direction
    new_facing = ""

    if degree == 0 or degree == 360 or degree == -360:
        new_facing = "N"
    if degree == 90 or degree == -270:
        new_facing = "E"
    if degree == 180 or degree == -180:
        new_facing = "S"
    if degree == 270 or degree == -90:
        new_facing = "W"

    return new_facing


with open("input.txt", "r") as file:
    data = file.read().splitlines()
    current_facing = "E"
    my_route = {"N": 0, "E": 0, "S": 0, "W": 0}
    for i in data:
        if "R" in i or "L" in i:
            current_facing = findDirection(current_facing, i)
        elif "F" in i:
            # update the coords in direction we are facing
            if current_facing == "N":
                my_route[current_facing] += int(i[1:])
            if current_facing == "E":
                my_route[current_facing] += int(i[1:])
            if current_facing == "S":
                my_route[current_facing] += int(i[1:])
            if current_facing == "W":
                my_route[current_facing] += int(i[1:])
        else:  # N O W S
            if "N" in i:
                my_route["N"] += int(i[1:])
            if "E" in i:
                my_route["E"] += int(i[1:])
            if "S" in i:
                my_route["S"] += int(i[1:])
            if "W" in i:
                my_route["W"] += int(i[1:])

    NS = abs(int(my_route["N"])-int(my_route['S']))
    EW = abs(int(my_route["E"])-int(my_route['W']))
    print(NS+EW)

    # Part 2
    current_facing = "E"
    my_route = {"N": 0, "E": 0, "S": 0, "W": 0}
    waypoint = {"N": 1, "E": 10, "S": 0, "W": 0}
    for i in data:
        if "R" in i or "L" in i:
            waypoint = rotateWaypoint(waypoint, i)
        elif "F" in i:

            my_route["N"] += waypoint["N"] * int(i[1:])
            my_route["E"] += waypoint["E"] * int(i[1:])
            my_route["S"] += waypoint["S"] * int(i[1:])
            my_route["W"] += waypoint["W"] * int(i[1:])

        else:  # N O W S
            if "N" in i:
                waypoint["N"] += int(i[1:])
            if "E" in i:
                waypoint["E"] += int(i[1:])
            if "S" in i:
                waypoint["S"] += int(i[1:])
            if "W" in i:
                waypoint["W"] += int(i[1:])

    NS = abs(int(my_route["N"])-int(my_route['S']))
    EW = abs(int(my_route["E"])-int(my_route['W']))
    print(NS+EW)
