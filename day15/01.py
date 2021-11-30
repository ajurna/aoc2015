from dataclasses import dataclass
from parse import compile
from itertools import combinations_with_replacement, product
from collections import Counter
import math

parser = compile('{}: capacity {}, durability {}, flavor {}, texture {}, calories {}')


@dataclass(frozen=True)
class Ingredient:
    name: str
    capacity: int
    durability: int
    flavor: int
    texture: int
    calories: int

    def mix(self, quantity):
        return (
            self.capacity * quantity,
            self.durability * quantity,
            self.flavor * quantity,
            self.texture * quantity
        )

    def mix_calories(self, quantity):
        return self.calories * quantity


ingredients = []
with open('01.txt') as f:
    for line in f.readlines():
        name, *numbers = parser.parse(line.strip())
        ingredients.append(Ingredient(name, *map(int, numbers)))
best_score = 0
best_500 = 0
for comb in combinations_with_replacement(ingredients, r=100):
    recipe = Counter(comb)
    if len(recipe) != len(ingredients):
        continue
    mix = [sum(x) for x in zip(*[ingredient.mix(amount) for ingredient, amount in recipe.items()])]
    if all([x > 0 for x in mix]):
        best_score = max(best_score, math.prod(mix))
        if sum([ingredient.mix_calories(amount) for ingredient, amount in recipe.items()]) == 500:
            best_500 = max(best_500, math.prod(mix))

print("Part 1:", best_score)
print("Part 2:", best_500)