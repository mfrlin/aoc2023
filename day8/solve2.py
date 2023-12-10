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

current_nodes = [n for n in mapping.keys() if n.endswith('A')]
cycles = []
for i, direction in enumerate(itertools.cycle(directions), 1):
    if not current_nodes:
        break
    new_current_nodes = []
    for current_node in current_nodes:
        index = 0
        if direction == 'R':
            index = 1
        current_node = mapping[current_node][index]
        if current_node.endswith('Z'):
            cycles.append(i)
            continue
        new_current_nodes.append(current_node)
    current_nodes = new_current_nodes

from math import lcm

print(lcm(*cycles))


