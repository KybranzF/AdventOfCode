import re

print("-----------Part 1-----------")
contains = {}
for line in open("input.txt","r"):
    m = re.split(" bags contain ", line.strip())
    bags = m[1].replace(" bags", '').replace(".", '').replace(" bag", '').replace('no other', '0 other'). split(', ')
    pairs = [bag.split(' ', maxsplit=1) for bag in bags]
    print(pairs)
    contains[m[0]] = [(int(child[0]), child[1]) for child in pairs]

def find_parents(child):
    parents = set()
    [parents.add(k) for k,v in contains.items() if child in [color for number, color in v]]
    parents.discard(child) # prevent infinite recursion
    return parents

def get_roots(color, tree):
    parents = find_parents(color)
    if parents:
        tree |= parents
        for p in parents:
            get_roots(p, tree)
    return tree

ancestry = get_roots("shiny gold", set())
print(len(ancestry))

print("-----------Part 2-----------")
def count_children(color):
    count = 1
    for quantity, color in contains[color]:
        if color != 'other':
            count += int(quantity) * count_children(color)
    return count

print(count_children("shiny gold")-1)