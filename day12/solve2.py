with open('small_input.txt') as f:
    lines = f.readlines()


class State:
    def __init__(self, state, position, groups, extended=0):
        self.state = state
        self.position = position
        self.groups = groups
        self.extended = extended

    def copy(self):
        return State(
            state=self.state[:],
            position=self.position,
            groups=self.groups[:],
            extended=self.extended,
        )


def check_valid(state: State, groups):
    # optimizations
    # length = int(len(state.state) // 5) + 1
    # start = (state.position // length) * length
    # end = start + length
    # number_of_current_springs = state.state[start:end].count('#')
    # number_of_current_dots = state.state[start:end].count('.')
    # number_of_springs = sum(groups[:len(groups)//5])
    # number_of_dots = length - number_of_springs
    # open_positions = state.state[start:end].count('?')
    # if number_of_current_springs > number_of_springs:
    #     return False
    # if number_of_current_springs + open_positions < number_of_springs:
    #     return False
    # if number_of_current_dots + open_positions < number_of_dots:
    #     return False
    #########
    #print('checking', state.state, state.position, state.groups, state.extended)
    while state.groups:
        g = state.groups[0]
        counted_springs = 0
        position = state.position
        while True:
            #print(state.state, position, state.groups)
            if position >= len(state.state):
                # we are at the end of state
                return g == counted_springs
            c = state.state[position]
            position += 1
            if c == '.':
                if not counted_springs:
                    # we didnt encounter any springs yet
                    state.position = position
                    continue
                else:
                    # we are past a group
                    if g == counted_springs:
                        # group is ok
                        state.groups.pop(0)
                        state.position = position
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
                elif counted_springs < g:
                    # if we are less next one must be #
                    state.state[position - 1] = '#'
                    counted_springs += 1
                elif counted_springs == g:
                    # we know that next one must be .
                    state.state[position - 1] = '.'
                    state.groups.pop(0)
                    state.position = position
                    break
                else:
                    # we are larger than group. not valid.
                    return False
    else:
        # we exhausted defined groups. check if there are additional springs ahead
        return state.state.count('#') == sum(groups * (state.extended + 1))




def check_solved(state, groups):
    if '?' in state.state:
        return False
    return state.state.count('#') == sum(groups)

n = 0
counter = 0
for line in lines:
    original_positions, groups = line.strip().split(' ')
    original_groups = list(map(int, groups.split(',')))
    groups = original_groups * 5
    # print(len(original_groups))
    # print(len(groups))
    # print(len(original_positions))
    positions = '?'.join([original_positions] * 5)
    # print(len(positions))
    springs_n = sum(groups)
    open_positions = positions.count('?')
    placed_springs = positions.count('#')
    springs_to_place = springs_n - placed_springs
    frontier = [State(list(positions), 0, groups[:])]
    solved_states = 0
    print(positions, groups)
    while frontier:
        state = frontier.pop()
        for c in ['#', '.']:
            new_state = state.copy()
            try:
                first_open = new_state.state.index('?')
            except ValueError:
                continue
            new_state.state[first_open] = c
            valid = check_valid(new_state, groups)
            #print(valid)
            #print('after', new_state.state, new_state.position, new_state.groups)
            if not valid:
                continue
            else:
                if check_solved(new_state, groups):
                    #print('solved')
                    solved_states += 1
                else:
                    #print('not solved')
                    frontier.append(new_state)
    
    print(solved_states)
    counter += solved_states
    n += 1
    print(n)
    

print(counter)
