with open("01.txt", 'r') as f:
    data = f.readlines()

# data = ['1x1x10']
total = 0
for present in data:
    l, w, h = map(int, present.strip().split('x'))
    presents = [l*w, w*h, h*l]
    slack = min(presents)
    total += sum(presents) * 2 + slack
print('Part 1:', total)

total = 0
for present in data:
    l, w, h = map(int, present.strip().split('x'))
    s, m, _ = sorted([l, w, h])
    ribbon = sum([s, s, m, m])
    bow = l * w * h
    total += ribbon + bow
print('Part 2:', total)
