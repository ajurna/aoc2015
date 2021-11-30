from dataclasses import dataclass


@dataclass
class Reindeer:
    name: str
    speed: int
    fly_time: int
    rest_time: int
    distance: int = 0
    state: str = 'flying'
    countdown: int = 0
    score: int = 0

    def __post_init__(self):
        self.countdown = self.fly_time

    def race(self):
        if self.state == 'flying':
            self.distance += self.speed
            self.countdown -= 1
        if self.state == 'resting':
            self.countdown -= 1
        if self.countdown == 0:
            if self.state == 'flying':
                self.state = 'resting'
                self.countdown = self.rest_time
            else:
                self.state = 'flying'
                self.countdown = self.fly_time

racers = []

with open('01.txt') as f:
    for line in f.readlines():
        name, _, _, speed, _, _, fly_time, *_, rest_time, _ = line.split()
        racers.append(Reindeer(name, int(speed), int(fly_time), int(rest_time)))

if __name__ == '__main__':
    for _ in range(2503):
        for reindeer in racers:
            reindeer.race()
        leading_distance = max([x.distance for x in racers])
        for racer in racers:
            if racer.distance == leading_distance:
                racer.score += 1

    racers.sort(key=lambda x: x.distance)
    print('Part 1:', racers[-1].distance)

    racers.sort(key=lambda x: x.score)
    print('Part 2:', racers[-1].score)