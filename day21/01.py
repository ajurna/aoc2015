from dataclasses import dataclass
from typing import Union, List, Tuple, Iterable


@dataclass
class Player:
    health: int = 100
    damage: int = 0
    defence: int = 0

    def add_equipment(self, items: Iterable['Equipment']):
        for item in items:
            self.damage += item.damage
            self.defence += item.armor

    def attack(self, enemy: 'Player'):
        enemy.health -= max(1, self.damage - enemy.defence)


@dataclass
class Equipment:
    name: str
    cost: int = 0
    damage: int = 0
    armor: int = 0


weapons = [
    Equipment('None', cost=0),
    Equipment('Dagger', cost=8, damage=4),
    Equipment('Shortsword', cost=10, damage=5),
    Equipment('Warhammer', cost=25, damage=6),
    Equipment('Longsword', cost=40, damage=7),
    Equipment('Greataxe', cost=74, damage=8),
]
armors = [
    Equipment('None', cost=0),
    Equipment('Leather', cost=13, armor=1),
    Equipment('Chainmail', cost=31, armor=2),
    Equipment('Splintmail', cost=53, armor=3),
    Equipment('Bandedmail', cost=75, armor=4),
    Equipment('Platemail', cost=102, armor=5),
]
rings = [
    Equipment('None', cost=0),
    Equipment('None', cost=0),
    Equipment('Damage +1', cost=25, damage=1),
    Equipment('Damage +2', cost=50, damage=2),
    Equipment('Damage +3', cost=100, damage=3),
    Equipment('Defense +1', cost=25, armor=1),
    Equipment('Defense +2', cost=50, armor=2),
    Equipment('Defense +3', cost=100, armor=3),
]
sets = [(a, b, c, d) for a in weapons for b in armors for c in rings for d in rings if c != d]

sets.sort(key=lambda x: x[0].cost + x[1].cost + x[2].cost + x[3].cost)
for e_set in sets:
    player = Player()
    player.add_equipment(e_set)
    enemy_boss = Player(health=103, damage=9, defence=2)
    while True:
        player.attack(enemy_boss)
        if enemy_boss.health <= 0:
            break
        enemy_boss.attack(player)
        if player.health <= 0:
            break
    if enemy_boss.health <= 0:
        print('Part 1:', sum([x.cost for x in e_set]))
        break

# sort sets from most to least expensive
sets.sort(key=lambda x: x[0].cost + x[1].cost + x[2].cost + x[3].cost, reverse=True)
for e_set in sets:
    player = Player()
    player.add_equipment(e_set)
    enemy_boss = Player(health=103, damage=9, defence=2)
    print()
    if e_set[0].name == 'None':
        continue
    while True:
        player.attack(enemy_boss)
        if enemy_boss.health <= 0:
            break
        enemy_boss.attack(player)
        if player.health <= 0:
            break
        print(player, enemy_boss)
    if player.health <= 0:
        print(player, enemy_boss)
        print(e_set)
        print('Part 2:', sum([x.cost for x in e_set]))
        break
