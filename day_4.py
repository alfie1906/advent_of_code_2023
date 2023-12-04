import re

from utils import read_input

def calculate_card_points(input_line: str) -> int:
    winning_numbers = extract_numbers(input_line.split(':')[1].split('|')[0])
    drawn_numbers = extract_numbers(input_line.split('|')[1])

    num_matches = len(winning_numbers.intersection(drawn_numbers))
    if num_matches != 0:
        return 2 ** (num_matches - 1)
    else:
        return 0

def extract_numbers(number_text: str) -> set:
    return set(map(int, re.findall(r'\d+', number_text)))

input = read_input(day=4)

p1_solution = sum(map(calculate_card_points, input))
print("Part 1 solution:", p1_solution)

copy_counts = [1 for _ in input]
max_index = len(input)

for index, input_line in enumerate(input):
    winning_numbers = extract_numbers(input_line.split(':')[1].split('|')[0])
    drawn_numbers = extract_numbers(input_line.split('|')[1])

    num_matches = len(winning_numbers.intersection(drawn_numbers))
    num_copies = copy_counts[index]

    copy_card_start = index + 1
    copy_card_end = index + num_matches + 1

    copy_counts[copy_card_start: copy_card_end] = [copies + num_copies for copies in copy_counts[copy_card_start: copy_card_end]]

p2_solution = sum(copy_counts)
print("Part 2 solution:", p2_solution)
