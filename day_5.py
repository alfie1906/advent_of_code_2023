import re

from utils import read_input
input = read_input(day=5)

class SourceDestinationLookup:
    def __init__(self, input_maps: list):
        self.input_map_data = [{
            'destination_range_start': int(input_map.split()[0]), 
            'source_range_start': int(input_map.split()[1]), 
            'range_length': int(input_map.split()[2])
            } 
            for input_map in input_maps
            ]

    def find_source_destination(self, source_number: int) -> int:
        for input_map in self.input_map_data:
            lower_source_limit = input_map['source_range_start']
            upper_source_limit = input_map['source_range_start'] + input_map['range_length']
            source_destination_offset = input_map['destination_range_start'] - input_map['source_range_start']

            if source_number >= lower_source_limit and source_number < upper_source_limit:
                return source_number + source_destination_offset
        
        return source_number 

def find_seed_location(seed_number: int, seed_soil_map: SourceDestinationLookup, soil_fertilizer_map: SourceDestinationLookup, fertilizer_water_map: SourceDestinationLookup, water_light_map: SourceDestinationLookup, light_temp_map: SourceDestinationLookup, temp_humidity_map: SourceDestinationLookup, humidity_loc_map: SourceDestinationLookup) -> int:
    soil_number = seed_soil_map.find_source_destination(seed_number)
    fertilizer_number = soil_fertilizer_map.find_source_destination(soil_number)
    water_number = fertilizer_water_map.find_source_destination(fertilizer_number)
    light_number = water_light_map.find_source_destination(water_number)
    temp_number = light_temp_map.find_source_destination(light_number)
    humidity_number = temp_humidity_map.find_source_destination(temp_number)
    location_number = humidity_loc_map.find_source_destination(humidity_number)

    return location_number

seed_numbers = list(map(int, re.findall(r'\d+', input[0])))
seed_soil_map = SourceDestinationLookup(input[3:23])
soil_fertilizer_map = SourceDestinationLookup(input[25:53])
fertilizer_water_map = SourceDestinationLookup(input[55:87])
water_light_map = SourceDestinationLookup(input[89:121])
light_temp_map = SourceDestinationLookup(input[123:166])
temp_humidity_map = SourceDestinationLookup(input[168:202])
humidity_loc_map = SourceDestinationLookup(input[204:])

seed_locations = list(map(lambda seed_number: find_seed_location(seed_number, seed_soil_map, soil_fertilizer_map, fertilizer_water_map, water_light_map, light_temp_map, temp_humidity_map, humidity_loc_map), seed_numbers))
print("Part 1 solution:", min(seed_locations))

"""
correct_seed_numbers = []
for pair_number in range(0, 10):
    initial_seed = seed_numbers[pair_number + (pair_number * 1)]
    seed_range = seed_numbers[1 + pair_number + (pair_number * 1)] 
    correct_seed_numbers += list(range(initial_seed, initial_seed + seed_range))
"""


class DestinationSourceLookup:
    def __init__(self, input_maps: list):
        self.input_map_data = [{
            'destination_range_start': int(input_map.split()[0]), 
            'source_range_start': int(input_map.split()[1]), 
            'range_length': int(input_map.split()[2])
            } 
            for input_map in input_maps
            ]

    def find_destination_source(self, destination_number: int) -> int:
        for input_map in self.input_map_data:
            lower_destination_limit = input_map['destination_range_start']
            upper_destination_limit = input_map['destination_range_start'] + input_map['range_length']
            destination_source_offset = input_map['source_range_start'] - input_map['destination_range_start']

            if destination_number >= lower_destination_limit and destination_number < upper_destination_limit:
                return destination_number + destination_source_offset
        
        return destination_number 

def find_location_seed(location_number: int, soil_seed_map: DestinationSourceLookup, fertilizer_soil_map: DestinationSourceLookup, water_fertilizer_map: DestinationSourceLookup, light_water_map: DestinationSourceLookup, temp_light_map: DestinationSourceLookup, humidity_temp_map: DestinationSourceLookup, loc_humidity_map: DestinationSourceLookup) -> int:
    humidity_number = loc_humidity_map.find_destination_source(location_number)
    temp_number = humidity_temp_map.find_destination_source(humidity_number)
    light_number = temp_light_map.find_destination_source(temp_number)
    water_number = light_water_map.find_destination_source(light_number)
    fertilizer_number = water_fertilizer_map.find_destination_source(water_number)
    soil_number = fertilizer_soil_map.find_destination_source(fertilizer_number)
    seed_number = soil_seed_map.find_destination_source(soil_number)
    
    return seed_number

seed_numbers = list(map(int, re.findall(r'\d+', input[0])))
soil_seed_map = DestinationSourceLookup(input[3:23])
fertilizer_soil_map = DestinationSourceLookup(input[25:53])
water_fertilizer_map = DestinationSourceLookup(input[55:87])
light_water_map = DestinationSourceLookup(input[89:121])
temp_light_map = DestinationSourceLookup(input[123:166])
humidity_temp_map = DestinationSourceLookup(input[168:202])
loc_humidity_map = DestinationSourceLookup(input[204:])

location_brackets = {int(humidity_loc.split()[1]): int(humidity_loc.split()[1]) + int(humidity_loc.split()[2]) for humidity_loc in input[204:]}
min_location_bracket_start = min(location_brackets.keys())
min_location_bracket_end = location_brackets[min_location_bracket_start]

seed_for_bracket_start = find_location_seed(min_location_bracket_start, soil_seed_map, fertilizer_soil_map, water_fertilizer_map, light_water_map, temp_light_map, humidity_temp_map, loc_humidity_map)
# 2792210896
seed_for_bracket_end = find_location_seed(min_location_bracket_end, soil_seed_map, fertilizer_soil_map, water_fertilizer_map, light_water_map, temp_light_map, humidity_temp_map, loc_humidity_map)
print(seed_for_bracket_start, seed_for_bracket_end)

loop_count = 0
while True:
    for pair_number in range(0, 10):
        initial_seed = seed_numbers[pair_number + (pair_number * 1)]
        seed_range = seed_numbers[1 + pair_number + (pair_number * 1)]
        seed_to_check = initial_seed + loop_count

        if loop_count >= seed_range:
            continue
        
        if seed_for_bracket_start <= seed_to_check <= seed_for_bracket_end:
            print("P2 solution:", find_seed_location(seed_to_check, seed_soil_map, soil_fertilizer_map, fertilizer_water_map, water_light_map, light_temp_map, temp_humidity_map, humidity_loc_map), seed_numbers)
            break
    
    loop_count += 1
    if loop_count % 1000000 == 0:
        print(loop_count)
