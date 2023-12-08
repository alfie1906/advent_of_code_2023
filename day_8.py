import re
import math

from utils import read_input
input = read_input(day=8)

def parse_instructions(input_line: str) -> dict:
    start = re.findall(r'\w+(?=\s)', input_line)[0]
    L = re.findall(r'(?<=\()\w+', input_line)[0] 
    R = re.findall(r'\w+(?=\))', input_line)[0]

    return start, L, R

def steps_to_z(location:str, instructions: dict, steps: list) -> int:
    step_count = 0
    while True:
        for step in steps:
            step_count += 1
            location = instructions[location][step]
            
        if location == 'ZZZ':
            break

    return step_count

steps = re.findall(r'\w', input[0])

instructions = {start: {'L': L, 'R': R} for start, L, R in [parse_instructions(input_line) for input_line in input[2:]]}

print("Part 1 solution:", steps_to_z('AAA', instructions, steps))

def steps_to_z(location:str, instructions: dict, steps: list) -> int:
    step_count = 0
    while True:
        for step in steps:
            step_count += 1
            location = instructions[location][step]
            
        if location[-1] == 'Z':
            break

    return step_count

start_locations = [node for node in instructions.keys() if node[-1] == 'A']
step_counts = list(map(lambda location: steps_to_z(location, instructions, steps), start_locations))

least_common_multiple = 1
for step_count in step_counts:
    least_common_multiple = least_common_multiple * step_count // math.gcd(least_common_multiple, step_count)

print("Part 2 solution:", least_common_multiple)
