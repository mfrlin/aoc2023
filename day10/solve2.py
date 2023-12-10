MAP = []
with open('input.txt') as f:
    lines = f.readlines()

starting_pos = None
for y, line in enumerate(lines):
    line = line.strip()
    print(line)
    try:
        x = line.index('S')
        starting_pos = (x, y)
    except:
        pass
    MAP.append(list(line))


CONNECTIONS = {
    'S': set(['N', 'S', 'E', 'W']),
    '|': set(['N', 'S']),
    '-': set(['E', 'W']),
    'L': set(['N', 'E']),
    'J': set(['N', 'W']),
    '7': set(['S', 'W']),
    'F': set(['S', 'E']),
    '.': set(),
}

def opposite(direction):
    return {
        'S': 'N',
        'N': 'S',
        'E': 'W',
        'W': 'E',
    }[direction]

def get_pipe(x, y):
    try:
        return MAP[y][x]
    except IndexError:
        return '.'


def find_next(x, y):
    next_positions = []
    pipe = get_pipe(x, y)
    connections = CONNECTIONS[pipe]
    for c in connections:
        nx, ny = x, y
        if c == 'N':
            ny -= 1
        elif c == 'S':
            ny += 1
        elif c == 'E':
            nx += 1
        elif c == 'W':
            nx -= 1
        else:
            raise ValueError()
        next_pipe = get_pipe(nx, ny)
        if opposite(c) in CONNECTIONS[next_pipe]:
            next_positions.append((nx, ny))
    return next_positions

def find_path():
    frontier = [[starting_pos]]  # list of paths
    target = starting_pos
    while frontier:
        path = frontier.pop(0)
        pos = path[-1]
        if len(path) == 1:
            originating_pos = pos
        else:
            originating_pos = path[-2]
        if pos == target and pos != originating_pos:
            return path
        for next_pos in find_next(*pos):
            if next_pos != originating_pos:
                new_path = path[::]
                new_path.append(next_pos)
                frontier.append(new_path)

path = find_path()
set_path = set(path)
inside = set()
for y, row in enumerate(MAP):
    is_inside = False
    for x, pipe in enumerate(row):
        if (x, y) in set_path:
            # are we "sliding" along the outside?
            if MAP[y][x] not in 'SF-7':  # if S is |, J or L you need to remove it
                is_inside = not is_inside 
        else:
            if is_inside:
                inside.add((x, y))



# VISUALIZING
# for y in range(len(MAP)):
#     row = []
#     for x in range(len(MAP[0])):
#         if (x, y) in set_path:
#             row.append(MAP[y][x])
#         else:
#             if (x, y) in inside:
#                 row.append('*')
#             else:
#                 row.append('O')
#     print(''.join(row))


# RESULT
print(len(inside))
