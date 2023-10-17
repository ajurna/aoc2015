from dataclasses import dataclass


@dataclass
class Point:
    row: int = 1
    col: int = 1

    def next(self):
        if self.row == 1:
            self.row = self.col + 1
            self.col = 1
        else:
            self.row -= 1
            self.col += 1
            

p = Point()
target = Point(2947, 3029)
number = 20151125
while True:
    if p == target:
        break
    p.next()
    number = (number * 252533) % 33554393
print("Part 1:", number)
