import math
from itertools import combinations


MAP = []
with open('input.txt') as f:
    lines = f.readlines()

galaxies = []
insert_rows = []
for y, line in enumerate(lines):
    line = line.strip()
    MAP.append(line)
    if len(set(line)) == 1:
        insert_rows.append(y)
    for x, c in enumerate(line):
        if c == '#':
            galaxies.append((x, y))

insert_columns = []
for i in range(len(MAP[0])):
    column = [row[i] for row in MAP]
    if len(set(column)) == 1:
        insert_columns.append(i)

new_galaxies = []
for x, y in galaxies:
    y += (1000000-1) * sum(1 for r in insert_rows if y > r)  # in PART 1 is 1 * sum(..)
    x += (1000000-1) * sum(1 for c in insert_columns if x > c)  # in PART 1 is 1 * sum(..)
    new_galaxies.append((x, y))



galaxy_pairs = list(combinations(new_galaxies, 2))


def get_distance(node1, node2):
    x1, y1 = node1
    x2, y2 = node2
    return abs(x2 - x1) + abs(y2 - y1)

counter = 0
for start, end in galaxy_pairs:
    counter += get_distance(start,end)

print('result', counter)