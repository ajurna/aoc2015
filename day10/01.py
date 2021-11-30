from collections import deque


def count_numbers(data: deque):
    out = deque()
    while data:
        f_c = data[0]
        count = 0
        while data and f_c == data[0]:
            data.popleft()
            count += 1
        out.append(count)
        out.append(f_c)
    return out


number = deque(map(int, "1113222113"))
for _ in range(40):
    number = count_numbers(number)
print('Part 1:', len(number))

for _ in range(10):
    number = count_numbers(number)
print('Part 2:', len(number))
