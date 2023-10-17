from itertools import combinations
from math import prod
presents = []

with open('01.txt') as f:
    for line in f.readlines():
        presents.append(int(line))

limit = sum(presents)//3
results = {}
for i in range(len(presents)):
    for items in combinations(presents, i):
        if sum(items) == limit:
            results[prod(items)] = items
    if len(results) > 0:
        break

print("Part 1:", min(results))

limit = sum(presents)//4
results = {}
for i in range(len(presents)):
    for items in combinations(presents, i):
        if sum(items) == limit:
            results[prod(items)] = items
    if len(results) > 0:
        break

print("Part 2:", min(results))