import re

from utils import read_input

input = read_input(day=2)

def get_game_id_if_possible(bag_line: str) -> int:
    game_id = int(re.findall(r'\d+', bag_line)[0])  
    bag_sets = re.split(r';|:', bag_line)[1:]
    
    if all(map(determine_set_possible, bag_sets)):
        return game_id
    else:
        return 0

def determine_set_possible(bag_set: str) -> bool:
    limit = {
        'red': 12,
        'green': 13,
        'blue': 14
        }
    
    for colour in ('red', 'green', 'blue'):
        cube_counts = re.findall(rf'\d+(?=\s{colour})', bag_set)
        if len(cube_counts) == 0:
            continue

        cube_counts = list(map(int, cube_counts))
        if any([cube_count > limit[colour] for cube_count in cube_counts]):
            return False
        
    return True
    
print("Part 1 solution:", sum(map(get_game_id_if_possible, input)))

def get_game_power(bag_line: str) -> int:
    min_red = get_colour_min(bag_line, 'red')
    min_green = get_colour_min(bag_line, 'green')
    min_blue = get_colour_min(bag_line, 'blue')
    
    return min_red * min_green * min_blue

def get_colour_min(bag_line: str, colour: str) -> int:
    cube_counts = re.findall(rf'\d+(?=\s{colour})', bag_line)
    if len(cube_counts) == 0:
        return 0
    else:
        cube_counts = list(map(int, cube_counts))
        return max(cube_counts)

print("Part 2 solution:", sum(map(get_game_power, input)))
