from collections import Counter

from parse import compile
parser = compile('Sue {}: {}: {}, {}: {}, {}: {}')
parser2 = compile('{}: {}')

sue_data = {}
with open('01.txt') as f:
    for line in f.readlines():
        line = line.strip()
        sue, *details = parser.parse(line)
        for thing, amount in zip(details[0::2], details[1::2]):
            amount = int(amount)
            if thing not in sue_data:
                sue_data[thing] = {}
                sue_data[thing][amount] = set()
            elif amount not in sue_data[thing]:
                sue_data[thing][amount] = set()
            sue_data[thing][amount].add(sue)

sue_sets = []
with open('01clues.txt') as f:
    for line in f.readlines():
        line = line.strip()
        thing, amount = parser2.parse(line)
        amount = int(amount)
        sue_sets.append(sue_data[thing][amount])
all_sues = []
for item in sue_sets:
    all_sues.extend(item)

print('Part 1:', sorted(Counter(all_sues).items(), key=lambda x: x[1])[-1][0])

sue_sets = []
with open('01clues.txt') as f:
    for line in f.readlines():
        line = line.strip()
        thing, amount = parser2.parse(line)
        amount = int(amount)
        if thing in ['cats', 'trees']:
            for extra_amount in [x for x in sue_data[thing].keys() if x > amount]:
                sue_sets.append(sue_data[thing][extra_amount])
        elif thing in ['pomeranians', 'goldfish']:
            for extra_amount in [x for x in sue_data[thing].keys() if x < amount]:
                sue_sets.append(sue_data[thing][extra_amount])
        else:
            sue_sets.append(sue_data[thing][amount])

all_sues = []
for item in sue_sets:
    all_sues.extend(item)

print('Part 2:', sorted(Counter(all_sues).items(), key=lambda x: x[1])[-1][0])