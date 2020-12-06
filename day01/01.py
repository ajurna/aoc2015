with open("01.txt", 'r') as f:
    data = f.read()

# data = '(()(()('
total = 0
for cha in data:
    if cha == '(':
        total += 1
    elif cha == ')':
        total -= 1
print('Part 1:', total)
total = 0
for idx, cha in enumerate(data):
    if cha == '(':
        total += 1
    elif cha == ')':
        total -= 1
    if total == -1:
        break
print('Part 2:', idx+1)