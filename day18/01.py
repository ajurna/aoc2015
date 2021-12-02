from copy import deepcopy
from typing import NamedTuple, List
from collections import Counter


class Point(NamedTuple):
    x: int
    y: int

    def __add__(self, other: 'Point'):
        return Point(self.x + other.x, self.y + other.y)


grid = []
with open('01.txt') as f:
    for line in f.readlines():
        grid.append(list(line.strip()))


def iterate_lights(old_grid: List[List[str]]) -> List[List[str]]:
    x_max = len(grid[0])
    y_max = len(grid)
    directions = [Point(x, y) for x in (-1, 0, 1) for y in (-1, 0, 1) if Point(x, y) != Point(0, 0)]
    new_grid = deepcopy(old_grid)
    search_area = [Point(x, y) for y in range(y_max) for x in range(x_max)]
    for p in search_area:
        lights = Counter([old_grid[sp.y][sp.x] for sp in
                          filter(lambda dp: 0 <= dp.x < x_max and 0 <= dp.y < y_max, [p + d for d in directions])])
        if new_grid[p.y][p.x] == '#':
            if 2 <= lights['#'] <= 3:
                new_grid[p.y][p.x] = '#'
            else:
                new_grid[p.y][p.x] = '.'
        else:
            if lights['#'] == 3:
                new_grid[p.y][p.x] = '#'
    return new_grid


def iterate_lights_part2(old_grid: List[List[str]]) -> List[List[str]]:
    x_max = len(grid[0])
    y_max = len(grid)
    old_grid[0][0] = '#'
    old_grid[0][x_max-1] = '#'
    old_grid[y_max-1][0] = '#'
    old_grid[y_max-1][x_max-1] = '#'
    directions = [Point(x, y) for x in (-1, 0, 1) for y in (-1, 0, 1) if Point(x, y) != Point(0, 0)]
    new_grid = deepcopy(old_grid)
    search_area = [Point(x, y) for y in range(y_max) for x in range(x_max)]
    for p in search_area:
        lights = Counter([old_grid[sp.y][sp.x] for sp in
                          filter(lambda dp: 0 <= dp.x < x_max and 0 <= dp.y < y_max, [p + d for d in directions])])
        if new_grid[p.y][p.x] == '#':
            if 2 <= lights['#'] <= 3:
                new_grid[p.y][p.x] = '#'
            else:
                new_grid[p.y][p.x] = '.'
        else:
            if lights['#'] == 3:
                new_grid[p.y][p.x] = '#'
    new_grid[0][0] = '#'
    new_grid[0][x_max-1] = '#'
    new_grid[y_max-1][0] = '#'
    new_grid[y_max-1][x_max-1] = '#'
    return new_grid


def print_grid(grid_data):
    for data in grid_data:
        print(''.join(data))
    print()


if __name__ == '__main__':
    part1_grid = deepcopy(grid)
    for _ in range(100):
        part1_grid = iterate_lights(part1_grid)
    g = []
    for li in part1_grid:
        g.extend(li)
    print('Part 1:', Counter(g)['#'])
    for _ in range(100):
        grid = iterate_lights_part2(deepcopy(grid))
    g = []
    for li in grid:
        g.extend(li)
    print('Part 2:', Counter(g)['#'])
