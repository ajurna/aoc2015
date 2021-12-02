from sympy import divisors
target = 36_000_000

for x in range(target):
    result = sum([y*10 for y in divisors(x)])
    if result >= target:
        part_1_result = x
        break
print('Part 1:', part_1_result)


for x in range(target):
    result = sum([y * 11 for y in divisors(x) if (x / y) <= 50])
    if result >= target:
        part_2_result = x
        break
print('Part 2:', part_2_result)
