import re
from utils import read_input

input = read_input(day=1)

def extract_first_and_last_digit(line: str) -> int:
    digits = re.findall(r'\d', line)
    first = digits[0]
    last = digits[-1]
    concatenated_number = first + last

    return int(concatenated_number)

row_numbers_part_1 = list(map(extract_first_and_last_digit, input))
part_1_solution = sum(row_numbers_part_1)
print("Part 1 solution =", part_1_solution)

def replace_overlapping_digit_text(line: str) -> str:
    overlapping_digit_replacements = {
        "oneight": "oneeight",
        "twone": "twoone",
        "threeight": "threeeight",
        "fiveight": "fiveeight",
        "sevenine": "sevennine",
        "eightwo": "eighttwo",
        "eighthree": "eightthree",
        "nineight": "nineeight"
        }

    for overlapping_digits, replacement in overlapping_digit_replacements.items():
        line = line.replace(overlapping_digits, replacement)

    return line

def convert_digit_text(digit: str) -> str:
    digit_lookup = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
        }

    if digit not in digit_lookup.keys():
        return digit
    else:
        return digit_lookup[digit]

def extract_first_and_last_digit_part_two(line: str) -> int:
    digits = re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine', line)
    digits = list(map(convert_digit_text, digits))

    first = digits[0]
    last = digits[-1]
    concatenated_number = first + last

    return int(concatenated_number)

input = list(map(replace_overlapping_digit_text, input))
row_numbers_part_2= list(map(extract_first_and_last_digit_part_two, input))
part_2_solution = sum(row_numbers_part_2)
print("Part 2 solution =", part_2_solution)
    