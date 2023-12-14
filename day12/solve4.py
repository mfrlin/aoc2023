with open('test_input.txt') as f:
    lines = f.readlines()


class State:
    def __init__(self, state, position, groups):
        self.state = state
        self.position = position
        self.groups = groups

    def copy(self):
        return State(
            state=self.state[:],
            position=self.position,
            groups=self.groups[:],
        )


def check_valid(state: State, groups):
    position = state.position
    while state.groups:
        g = state.groups[0]
        counted_springs = 0
        while True:
            #print('checking:', state.state, position, state.groups)
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
                if counted_springs > g:
                    return False
                continue
            else:
                # we are at ?
                if not counted_springs:
                    # we are not in the group so we are valid either way
                    return True
                elif counted_springs < g:
                    # if we are less next one must be #
                    state.state[position - 1] = '#'
                    counted_springs += 1
                    continue
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
        return not bool(state.state[position:].count('#'))




def check_solved(state, groups):
    if '?' in state.state:
        return False
    return state.state.count('#') == sum(groups)

EXTEND = 5
n = 0
counter = 0
for line in lines:
    original_positions, groups = line.strip().split(' ')
    original_groups = list(map(int, groups.split(',')))
    groups = original_groups * EXTEND
    positions = '?'.join([original_positions] * EXTEND)
    frontier = [State(list(positions), 0, groups[:])]
    solved_states = []
    print(positions, groups)
    ops = 0
    while frontier:
        state = frontier.pop()
        for s, c in zip([state, state.copy()], ['#', '.']):
            if c == '#' and not s.groups:
                # if no groups dont bother with #
                continue
            first_open = s.state.index('?')
            s.state[first_open] = c
            valid = check_valid(s, groups)
            # print('is_valid:', valid)
            # print('after check:', s.state, s.position, s.groups)
            if not valid:
                if '?' not in s.state and s.groups:
                    # if # is not valid because it couldn't fill groups don't try with .
                    break
                continue
            else:
                if check_solved(s, groups):
                    solved_states.append(s.state)
                else:
                    ops += 1
                    frontier.append(s)
        # input()
    
    print(len(solved_states))
    #counter += solved_states
    # for s in solved_states:
    #     print(''.join(s))
    #n += 1
    #print(n)
    print(ops)
    

#print(counter)
