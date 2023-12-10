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

frontier = [(0, starting_pos, starting_pos)]  # list of tuples(int, tuple, tuple) (path_len, originating position, position_to_process)
seen = set()
while frontier:
    path_len, originating_pos, pos = frontier.pop(0)
    print('processing', pos)
    if pos in seen:
        print('found end', pos, path_len)
        break
    else:
        seen.add(pos)
    for next_pos in find_next(*pos):
        if next_pos != originating_pos:
            print('adding to frontier', next_pos)
            frontier.append((path_len+1, pos, next_pos))
