

with open("01.txt", 'r') as f:
    data = f.readlines()

# data = ['qjhvhtzxzqqjkmpb']
banned_sequence = ['ab', 'cd', 'pq', 'xy']
total = 0
for name in data:
    if len(list(filter(lambda x: x in 'aeiou', name))) < 3:
        continue
    if not any([a==b for a, b in zip(name, name[1:])]):
        continue
    if any([x in name for x in banned_sequence]):
        continue
    total += 1
print('Part 1:', total)
total = 0
for name in data:
    if not any([name.count(f'{a}{b}') >= 2 for a, b in zip(name, name[1:])]):
        continue
    if not any([a==c and a != b for a, b, c in zip(name, name[1:], name[2:])]):
        continue
    total += 1

print('Part 1:', total)