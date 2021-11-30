from collections import defaultdict
from itertools import permutations


table_data = defaultdict(dict)
with open('01.txt') as f:
    for line in f.readlines():
        line = line.strip()
        person_a, _, gain_lose, amount, *_, person_b = line.split()
        person_b = person_b[:-1]
        if gain_lose == 'gain':
            amount = int(amount)
        else:
            amount = -abs(int(amount))
        table_data[person_a][person_b] = amount


def get_happiness(data):
    max_happiness = 0
    for layout in permutations(data.keys()):
        total = 0
        for person in layout:
            index = layout.index(person)
            index_right = index + 1
            if index_right> len(layout)-1:
                index_right = 0
            total += data[person][layout[index_right]]
            total += data[person][layout[index - 1]]
        max_happiness = max(total, max_happiness)
    return max_happiness


if __name__ == '__main__':
    happiness = get_happiness(table_data)
    print('Part 1:', happiness)
    for person in list(table_data.keys()):
        table_data['me'][person] = 0
        table_data[person]['me'] = 0
    happiness = get_happiness(table_data)
    print('Part 2:', happiness)

