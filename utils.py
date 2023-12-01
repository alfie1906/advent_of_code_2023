def read_input(day: int) -> list:
    with open(f'data/day_{day}.txt') as data_file:
        data = data_file.read()
        data_lines = data.split('\n')
    
    return data_lines