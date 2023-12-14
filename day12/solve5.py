def dfs(springs: str, groups: tuple[int], memo=None) -> int:
    print('processing', springs, groups)
    if memo is None:
        # Prepare a dict for saving results
        memo = dict()
    # Edge conditions
    if not len(springs): # reached the end of springs
        r = int(len(groups) == 0)
        print('returning', r)
        return r
    if not len(groups): # reached the end of groups
        r = int(springs.count('#') == 0)
        print('returning', r)
        return r
    if memo.get((springs, groups)) is not None:
        r = memo[(springs, groups)]
        print('got from memo', springs, groups, r)
        return r

    g = groups[0] # This is the size of the next group we're trying to fill
    # Can we have a potential group of size g?
    validGroup = (
        g <= len(springs) # We need enough spaces available
        and springs[:g].count('.') == 0 # No dots in the group (only # and ?)
        and springs[g:g+1] != '#' # Cannot end with # (only ? or . or nothing(eol))
    )
    print('valid group', validGroup)
    result = 0

    # == Recursion ==
    # If first character a dot or a ? you pretend is a dot
    # we can only skip it without filling any group
    if springs[0] in '.?':
        result += dfs(springs[1:], groups, memo)
    # If the first character is a # or a ? you pretend is a #
    # we can maybe fill a group of size g
    if springs[0] in '#?' and validGroup:
        result += dfs(springs[g+1:], groups[1:], memo)
    
    # Save result for future use
    print('saved to memo', springs, groups, result)
    memo[(springs, groups)] = result
    return result
     
#print(dfs('?????.?#??????????.?#??????????.?#??????????.?#??????????.?#????', (1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1)))
"""
 |???.###|edge cases
1|10000  |0
1|  100 0|0
3|    1 0|0
-+-------+-
 |0000000|1
"""

print(dfs('?###????????', (3,2,1)))
"""
 |????.###|edge cases
1|310000  |0
1|  2100 0|0
3|    11 0|0
-+-------+-
 |00000000|1
"""
