import re

from utils import read_input
input = read_input(day=9)

def calc_next_value(history: str) -> int:
    sequence = list(map(int, re.findall(r'-?\d+', history)))
    all_differences = []
    all_differences.append(sequence)

    differences = sequence
    while differences:
        differences = calculate_differences(differences)
        all_differences.append(differences)

        if all(value == 0 for value in differences):
            break 
    
    all_differences = all_differences[::-1]
    for index, difference_list in enumerate(all_differences[:-1]):
        final_value = difference_list[-1]
        next_final_value = all_differences[index+1][-1]
        change = next_final_value + final_value
        all_differences[index+1].append(change)

    return change
    
def calculate_differences(sequence: list) -> list:
    differences = []
    for index, value in enumerate(sequence[:-1]):
        next_value = sequence[index+1]
        differences.append(next_value-value)
    
    return differences

final_values = list(map(calc_next_value, input))
print("Part 1 solution", sum(final_values))

def calc_first_value(history: str) -> int:
    sequence = list(map(int, re.findall(r'-?\d+', history)))
    all_differences = []
    all_differences.append(sequence)

    differences = sequence
    while differences:
        differences = calculate_differences(differences)
        all_differences.append(differences)

        if all(value == 0 for value in differences):
            break
    
    all_differences = all_differences[::-1]
    for index, difference_list in enumerate(all_differences[:-1]):
        first_value = difference_list[0]
        next_first_value = all_differences[index+1][0]
        change = next_first_value - first_value
        all_differences[index+1].insert(0, change)

    return change

first_values = list(map(calc_first_value, input))
print("Part 2 solution", sum(first_values))
