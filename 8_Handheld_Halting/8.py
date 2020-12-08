#!/usr/bin/env python3.9

with open("input.txt", "r") as file:
    data = file.read().splitlines()

instructions = []
for x in data:
    instructions.append(x.split())


def find_value(value):
    rvalue = ''
    if "+" in value:
        rvalue = int(value[1:])
    elif "-" in value:
        rvalue = -int(value[1:])
    return rvalue


def exec(instructions):
    # get all instructions
    number_of_instructions = len(instructions)
    success = False
    acc = 0
    next = 0
    db = []
    while next not in db:
        if number_of_instructions == next:
            success = True
            break
        op, offset = instructions[next]
        db.append(next)
        offsetval = offset[0] == '+' and int(offset[1:]) or -int(offset[1:])
        # offsetval = find_value(offset)
        # exit(0)
        if op == 'acc':
            next += 1
            acc += offsetval
        elif op == 'jmp':
            next += offsetval
        else:
            next += 1

    return acc, success


# p 1
resultP1 = run(instructions)[0]
print(resultP1)

# p 2
jmp_indexes = (i for i, instruction in enumerate(instructions)
               if instruction[0] == "jmp")

for index in jmp_indexes:
    _, offset = instructions[index]
    # flip to a nop
    instructions[index] = ("nop", offset)
    # print(instructions)
    acc, success = exec(instructions)
    # print(acc,index)
    if success:
        print(acc)
        break
    # if it does not work flip back
    instructions[index] = ("jmp", offset)
