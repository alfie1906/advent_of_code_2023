import re
from math import floor, ceil
from typing import Tuple
import numpy as np

from utils import read_input
input = read_input(day=6)

def find_num_options(total_time: int, distance: int) -> int:
    solution_1, solution_2 = solve_quad_equation(total_time, distance)
    num_options = abs(floor(solution_2) - ceil(solution_1)) - 1

    return num_options

def solve_quad_equation(total_time: int, distance: int) -> Tuple:
    """ 
    Problem can be represented as quadratic equation charge_time^2 - total_time*charge_time + distance. Find the solutions.
    a = 1
    b = -total_time
    c = distance
    """
    b_squared = total_time ** 2
    four_ac = 4 * 1 * distance
    two_a = 2 * 1
    solution_1 = (total_time + ((b_squared - four_ac) ** 0.5)) / two_a
    solution_2 = (total_time - ((b_squared - four_ac) ** 0.5)) / two_a

    return solution_1, solution_2

times = list(map(int, re.findall(r'\d+', input[0])))
distances = list(map(int, re.findall(r'\d+', input[1])))

options_per_race = list(map(lambda _: find_num_options(_[0], _[1]), zip(times, distances)))
print("Part 1 solution:", np.prod(options_per_race))

p2_time = int(''.join(map(str, times)))
p2_distance  = int(''.join(map(str, distances)))

print("Part 2 solution:", find_num_options(p2_time, p2_distance))
