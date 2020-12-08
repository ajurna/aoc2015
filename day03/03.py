from collections import deque
from typing import NamedTuple

with open("01.txt", 'r') as f:
    data = f.read()


class Point(NamedTuple):
    x: int
    y: int

    def east(self):
        return Point(self.x, self.y + 1)
    def south(self):
        return Point(self.x - 1, self.y)
    def west(self):
        return Point(self.x, self.y - 1)
    def north(self):
        return Point(self.x + 1, self.y)
    def move(self, d):
        if d == '>':
            return self.east()
        elif d == 'v':
            return self.south()
        elif d == '<':
            return self.west()
        elif d == '^':
            return self.north()

visited = {Point(0,0)}
total = 1


# data = '^v^v^v^v^v'
current_position = Point(0,0)
for d in data:
    current_position = current_position.move(d)

    if current_position in visited:
        continue
    else:
        visited.add(current_position)
print("Part 1:", len(visited))

robo = Point(0, 0)
santa = Point(0, 0)
visited = {Point(0, 0)}
queue = deque(data)
while queue:
    santa_dir = queue.popleft()
    robo_dir = queue.popleft()
    santa = santa.move(santa_dir)
    robo = robo.move(robo_dir)
    visited.add(santa)
    visited.add(robo)

print("Part 2:", len(visited))