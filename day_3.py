import re
import pandas as pd

from utils import read_input

input = read_input(day=3)

def extract_part_number_sum(input: list, input_line: str, line_number: int) -> int:
    number_data = get_number_data(input_line)

    return sum([number['value'] for number in number_data if is_part_number(input, number, line_number)])

def get_number_data(input_line: str) -> list:
    line_length = len(input_line)

    number_data = []
    for number in re.finditer(r'\d+', input_line):
        start_index = number.start(0) - 1
        if start_index < 0:
            start_index = 0
        
        end_index = number.end(0) + 1
        if end_index > line_length + 1:
            end_index = line_length + 1

        number_data.append({
            'value': int(number[0]),
            'start': start_index,
            'end': end_index
            })

    return number_data

def is_part_number(input: list, number_data: dict, line_number: int) -> bool:
    start = number_data['start']
    end = number_data['end']
    
    max_index = len(input)

    for line_index in [line_index for line_index in range(line_number-1, line_number+2) if line_index not in (-1, max_index)]:
        adjacent_data = input[line_index][start:end]
        if any(special_char in adjacent_data for special_char in '%|/|&|\+|#|-|\*|$|@|='):
            return True

p1_solution = sum([extract_part_number_sum(input, input_line, line_number) for line_number, input_line in enumerate(input)])
print("Part 1 solution:", p1_solution)

def collect_gear_data(input: list, input_line: str, line_number: int) -> int:
    number_data = get_number_data(input_line)
    gear_data = [get_adjacent_gear_data(input, number, line_number) for number in number_data]
    flattened_gear_data = [item for row in gear_data for item in row]
    
    return flattened_gear_data

def get_adjacent_gear_data(input: list, number_data: dict, line_number: int) -> bool:
    start = number_data['start']
    end = number_data['end']
    
    max_index = len(input)
    
    gear_data = []
    for line_index in [line_index for line_index in range(line_number-1, line_number+2) if line_index not in (-1, max_index)]:
        adjacent_data = input[line_index][start:end]
        if '*' in adjacent_data:
            gear_matches = re.finditer(r'\*', adjacent_data)
            gear_coordinates = [f'{line_index},{start+gear.start(0)}' for gear in gear_matches]

            gear_data += [{
                'coordinates': coordinates,
                'part_number': number_data['value']
                } for coordinates in gear_coordinates]
        
    return gear_data

flattened_gear_data = [item for row in [collect_gear_data(input, input_line, line_number) for line_number, input_line in enumerate(input)] for item in row]

gear_dict = {}
for gear in flattened_gear_data:
    coordinates = gear['coordinates']
    adjacent_part_number = gear['part_number']

    if coordinates not in gear_dict.keys():
        gear_dict[coordinates] = {
            'adjacent_part_numbers': [adjacent_part_number],
            'part_count': 1
            }
    else:
        gear_dict[coordinates]['adjacent_part_numbers'].append(adjacent_part_number)
        gear_dict[coordinates]['part_count'] += 1
        
gear_ratios = []
for gear, data in gear_dict.items():
    if data['part_count'] == 2:
        adjacent_parts = data['adjacent_part_numbers']
        gear_ratio = adjacent_parts[0] * adjacent_parts[1]
        gear_ratios.append(gear_ratio)

print("Part 2 solution:", sum(gear_ratios))
