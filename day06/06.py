import re

parse = re.compile(
    r'(?P<action>turn (?:on|off)|toggle) (?P<from_x>\d+),(?P<from_y>\d+) through (?P<to_x>\d+),(?P<to_y>\d+)'
)
with open("01.txt", 'r') as f:
    data = f.readlines()

grid = [[False for _ in range(1000)] for _ in range(1000)]

for line in data:
    # turn off 660,55 through 986,197
    action, from_x, from_y, to_x, to_y = parse.match(line).groups()
    for x in range(int(from_x), int(to_x)+1):
        for y in range(int(from_y), int(to_y)+1):
            if action == 'turn on':
                grid[y][x] = True
            elif action == 'turn off':
                grid[y][x] = False
            elif action == 'toggle':
                grid[y][x] = not grid[y][x]

print("Part 1:", sum([sum(x) for x in grid]))

grid = [[0 for _ in range(1000)] for _ in range(1000)]

for line in data:
    # turn off 660,55 through 986,197
    action, from_x, from_y, to_x, to_y = parse.match(line).groups()
    for x in range(int(from_x), int(to_x)+1):
        for y in range(int(from_y), int(to_y)+1):
            if action == 'turn on':
                grid[y][x] += 1
            elif action == 'turn off':
                if grid[y][x] > 0:
                    grid[y][x] -= 1
            elif action == 'toggle':
                grid[y][x] += 2
print("Part 2:", sum([sum(x) for x in grid]))