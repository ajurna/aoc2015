import re
from typing import NamedTuple

from parse import compile


class Transformation(NamedTuple):
    inp: str
    out: str


parser = compile('{} => {}')
transformations = []
with open('01.txt') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        if line == '':
            break
        inp, out = parser.parse(line)
        transformations.append(Transformation(inp, out))
    original_molecule = lines[-1].strip()

results = set()
atoms = set([x.inp for x in transformations])

molecule = []
parse_string = original_molecule
while parse_string:
    try:
        if parse_string[1].islower():
            atom = parse_string[:2]
            parse_string = parse_string[2:]
            molecule.append(atom)
        else:
            molecule.append(parse_string[0])
            parse_string = parse_string[1:]
    except IndexError:
        molecule.append(parse_string)
        parse_string = ''


for ind, cha in enumerate(molecule):
    for transform in transformations:
        results.add(''.join([
            *molecule[:ind],
            transform.out if molecule[ind] == transform.inp else molecule[ind],
            *molecule[ind+1:]
        ]))
results.remove(original_molecule)
print('Part 1:', len(results))


molecule = original_molecule[::-1]
reps = {x.out[::-1]: x.inp[::-1] for x in transformations}

count = 0
while molecule != 'e':
    molecule = re.sub('|'.join(reps.keys()), lambda x: reps[x.group()], molecule, 1)
    count += 1

print('Part 1:', count)
