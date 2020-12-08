with open('01.txt', 'r') as f:
    data = f.readlines()

raw = 0
par = 0
for line in data:
    line = line.strip()
    raw += len(line)
    par += len(eval(line))
print("Part 1:", raw-par)

print(sum(2+s.count('\\')+s.count('"') for s in open('01.txt')))