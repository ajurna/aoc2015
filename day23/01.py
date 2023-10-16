from typing import NamedTuple


class Instruction(NamedTuple):
    instruction: str
    register: str
    offset: int = 0


program = []
with open("01.txt", "r") as f:
    for line in f.readlines():
        line = line.strip()
        offset = 0
        if ',' in line:
            line, offset = line.split(', ')
        inst, reg = line.split()
        if inst == 'jmp':
            program.append(Instruction(inst, '', int(reg)))
        else:
            program.append(Instruction(inst, reg, int(offset)))


def run_program(registers):
    cursor = 0
    while cursor < len(program):
        current = program[cursor]
        match current.instruction:
            case 'hlf':
                registers[current.register] = registers[current.register] // 2
                cursor += 1
            case 'tpl':
                registers[current.register] = registers[current.register] * 3
                cursor += 1
            case 'inc':
                registers[current.register] += 1
                cursor += 1
            case 'jmp':
                cursor += current.offset
            case 'jie':
                if registers[current.register] % 2 == 0:
                    cursor += current.offset
                else:
                    cursor += 1
            case 'jio':
                if registers[current.register] == 1:
                    cursor += current.offset
                else:
                    cursor += 1
    return registers


print("Part 1:", run_program({
    'a': 0,
    'b': 0
})['b'])

print("Part 2:", run_program({
    'a': 1,
    'b': 0
})['b'])