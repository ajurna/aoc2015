import re

data = """123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i
i -> j"""
data = data.split('\n')

with open("02.txt", 'r') as f:
    data = f.readlines()

parse_1 = re.compile(r'(?P<x>\w+) (?P<op>\w+) (?P<y>\w+) -> (?P<d>\w+)')
def check_val(dig, storage):
    if not dig.isdigit():
        if dig in storage:
            return True, storage[dig]
        else:
            return False, 0
    else:
        return True, int(dig)

graf = {}
while data:
    inst = data.pop(0).strip()

    if match := parse_1.match(inst):
        x, op, y, dest = match.groups()
        valid, x = check_val(x, graf)
        if not valid:
            data.append(inst)
            continue
        valid, y = check_val(y, graf)
        if not valid:
            data.append(inst)
            continue
        if 'LSHIFT' in inst:
            graf[dest] = x << y
        elif 'RSHIFT' in inst:
            graf[dest] = x >> y
        elif 'OR' in inst:
            graf[dest] = x | y
        elif 'AND' in inst:
            graf[dest] = x & y
    elif 'NOT' in inst:
        _, x, _, dest = inst.split()
        valid, x = check_val(x, graf)
        if not valid:
            data.append(inst)
            continue
        graf[dest] = ~x & 0xFFFF
    else:
        x, dest = inst.split(' -> ')
        valid, x = check_val(x, graf)
        if not valid:
            data.append(inst)
            continue
        graf[dest] = int(x)



print("Part 2:", graf['a'])