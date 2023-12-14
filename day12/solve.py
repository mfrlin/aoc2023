with open('test_input.txt') as f:
    lines = f.readlines()


def check_valid(state, groups):
    # optimizations
    number_of_current_springs = state.count('#')
    number_of_springs = sum(groups)
    open_positions = state.count('?')
    if number_of_springs > number_of_springs:
        return False

    if number_of_current_springs + open_positions < number_of_springs:
        return False
    ############

    position = 0
    for g in groups:
        counted_springs = 0
        while True:
            # print(state, position)
            if position >= len(state):
                # we are at the end of state
                return g == counted_springs
            c = state[position]
            position += 1
            if c == '.':
                if not counted_springs:
                    # we didnt encounter any springs yet
                    continue
                else:
                    # we are past a group
                    if g == counted_springs:
                        # group is ok
                        break
                    # group not ok, not valid
                    return False
            elif c == '#':
                counted_springs += 1
            else:
                # we are at ?
                if not counted_springs:
                    # we are not in the group so we are valid either way
                    return True
                elif counted_springs <= g:
                    # if we are less or equal in group we are valid
                    return True
                else:
                    # we are larger than group. not valid.
                    return False
    else:
        # we exhausted defined groups. check if there are additional springs ahead
        return state.count('#') == sum(groups)

# valid = check_valid(
#     [
#         '#', '.', '#', '.', '#', '#', '#',
#         '.', '.', '#', '.', '#', '#', '#',
#         '#', '.', '#', '.', '#', '#', '#',
#         '#', '.', '#', '.', '#', '#', '#',
#         '#', '.', '#', '.', '#', '#', '#',
#     ],
#     [1, 1, 3, 1, 1, 3, 1, 1, 3, 1, 1, 3, 1, 1, 3])
# print(valid)
# raise ValueError()



def check_solved(state, groups):
    if '?' in state:
        return False
    return state.count('#') == sum(groups)

counter = 0
all_solved_states = []
for line in lines:
    positions, groups = line.strip().split(' ')
    groups = list(map(int, groups.split(',')))
    springs_n = sum(groups)
    open_positions = positions.count('?')
    placed_springs = positions.count('#')
    springs_to_place = springs_n - placed_springs
    frontier = [list(positions)]
    solved_states = []
    while frontier:
        state = frontier.pop()
        for c in ['#', '.']:
            new_state = state[:]
            try:
                first_open = new_state.index('?')
            except ValueError:
                continue
            new_state[first_open] = c
            valid = check_valid(new_state, groups)
            # print('valid:', valid)
            if not valid:
                continue
            else:
                if check_solved(new_state, groups):
                    solved_states.append(new_state)
                else:
                    frontier.append(new_state)

    counter += len(solved_states)

    print(positions, groups)
    print(len(solved_states))
    all_solved_states.append(solved_states)

set_states = set()
all_solved_sets = []
for solved_states in all_solved_states:
    set_states = set()
    for state in solved_states:
        set_states.add(''.join(state[:12]))
    all_solved_sets.append(set_states)

for s in all_solved_sets:
    print(s)
    print(len(s))
print(counter)






