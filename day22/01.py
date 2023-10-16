from copy import deepcopy
from dataclasses import dataclass, field
from collections import deque
from typing import Deque


@dataclass
class Player:
    health: int = 100
    damage: int = 0
    defence: int = 0
    mana: int = 500
    shielded: int = 0
    poisoned: int = 0
    recharging: int = 0

    def attack(self, enemy: 'Player'):
        enemy.health -= max(1, self.damage - enemy.defence)

    def process_effects(self):
        self.defence = 7 if self.shielded else 0
        if self.poisoned:
            self.health -= 3
        if self.recharging:
            self.mana += 101
        if self.shielded:
            self.shielded -= 1
        if self.poisoned:
            self.poisoned -= 1
        if self.recharging:
            self.recharging -= 1


@dataclass
class Boss(Player):
    pass


@dataclass
class State:
    player: Player
    boss: Boss
    mana_used = 0
    spells_cast: list = field(default_factory=list)


@dataclass
class Spell:
    cost: int

    def effect(self, player: Player, enemy: Player):
        pass

    def castable(self, state: State):
        return state.player.mana > self.cost


@dataclass
class MagicMissile(Spell):
    cost: int = 53

    def effect(self, player: Player, enemy: Player):
        player.mana -= self.cost
        enemy.health -= 4


@dataclass
class Drain(Spell):
    cost: int = 73

    def effect(self, player: Player, enemy: Player):
        player.mana -= self.cost
        player.health += 2
        enemy.health -= 2


@dataclass
class Shield(Spell):
    cost: int = 113

    def effect(self, player: Player, enemy: Player):
        player.mana -= self.cost
        player.shielded = 6
        player.defence = 7

    def castable(self, state: State):
        return state.player.mana > self.cost and state.player.shielded < 1


@dataclass
class Poison(Spell):
    cost: int = 173

    def effect(self, player: Player, enemy: Player):
        player.mana -= self.cost
        enemy.poisoned = 6

    def castable(self, state: State):
        return state.player.mana > self.cost and state.boss.poisoned < 1


@dataclass
class Recharge(Spell):
    cost: int = 229

    def effect(self, player: Player, enemy: Player):
        player.mana -= self.cost
        player.recharging = 5

    def castable(self, state: State):
        return state.player.mana > self.cost and state.player.recharging < 1


def play_game(hard=False):
    game = State(Player(health=50, mana=500), Boss(health=58, damage=9))
    spells = [MagicMissile(), Drain(), Shield(), Poison(), Recharge()]
    queue: Deque[State] = deque()
    queue.append(game)
    while queue:
        state = queue.popleft()
        state.player.process_effects()
        state.boss.process_effects()
        if state.boss.health <= 0:
            continue
        if hard:
            state.player.health -= 1
            if state.player.health <= 0:
                continue

        valid_spells = [s for s in spells if s.castable(state)]
        if valid_spells:
            for valid_spell in valid_spells:
                new_state = deepcopy(state)
                valid_spell.effect(new_state.player, new_state.boss)
                new_state.spells_cast.append(valid_spell)
                new_state.mana_used += valid_spell.cost
                # Boss turn
                new_state.player.process_effects()
                new_state.boss.process_effects()
                if new_state.boss.health <= 0:
                    return new_state.mana_used
                new_state.boss.attack(new_state.player)
                if new_state.player.health <= 0:
                    continue

                queue.append(new_state)


print("Part 1:", play_game())
print("Part 2:", play_game(hard=True))
