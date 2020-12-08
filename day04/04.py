import hashlib

i = 0
while True:
    if hashlib.md5(f"iwrupvqb{i}".encode()).hexdigest().startswith('00000'):
        break
    i += 1
print("Part 1:", i)

while True:
    if hashlib.md5(f"iwrupvqb{i}".encode()).hexdigest().startswith('000000'):
        break
    i += 1
print("Part 2:", i)