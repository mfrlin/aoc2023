import itertools


with open('input.txt') as f:
    lines = f.readlines()

mapping = {}
directions = lines[0].strip()
for line in lines[2:]:
    node, rest = line.split('=')
    node = node.strip()
    rest = rest.replace('(', '')
    rest = rest.replace(')', '')
    left_edge, right_edge = rest.split(',')
    left_edge = left_edge.strip()
    right_edge = right_edge.strip()
    mapping[node] = (left_edge, right_edge)

current_node = 'AAA'
for i, direction in enumerate(itertools.cycle(directions)):
    if current_node == 'ZZZ':
        print(i)
        break
    index = 0
    if direction == 'R':
        index = 1
    current_node = mapping[current_node][index]
