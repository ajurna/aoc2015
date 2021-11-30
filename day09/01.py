from itertools import permutations
from math import inf
data = {}
# example 1
filename = "01ex01.txt"
# day 01 data
filename = "01.txt"

with open(filename) as f:
    for line in f.readlines():
        places, distance = line.split(' = ')
        distance = int(distance)
        place_a, place_b = places.split(' to ')
        if place_a not in data:
            data[place_a] = {}
        if place_b not in data:
            data[place_b] = {}
        data[place_a][place_b] = distance
        data[place_b][place_a] = distance

destinations = data.keys()
best_score = inf
worst_score = 0
for combo in permutations(destinations):
    score = 0
    plan = list(combo)
    position = plan.pop(0)
    while plan:
        next_pos = plan.pop(0)
        score += data[position][next_pos]
        position = next_pos
    best_score = min(score, best_score)
    worst_score = max(score, worst_score)
    # print(combo, score)
print("Part 1:", best_score)
print("Part 2:", worst_score)
