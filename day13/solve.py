with open('input.txt') as f:
    lines = f.readlines()

patterns = []
new_pattern = []
for line in lines:
    line = line.strip()
    if line == '':
        patterns.append(new_pattern)
        new_pattern = []
        continue
    new_pattern.append(list(line))
patterns.append(new_pattern)

def print_pattern(pattern):
    for row in pattern:
        print(''.join(row))

def check_horizontal(pattern, original_result=None):
    for i in range(1, len(pattern)):
        j = 1
        while True:
            if i - j < 0 or i + j - 1 >= len(pattern):
                if i * 100 == original_result:
                    break
                return i * 100
            if pattern[i-j] != pattern[i+j-1]:
                break
            j += 1

def column(pattern, i):
    c = []
    for row in pattern:
        c.append(row[i])
    return c

def check_vertical(pattern, original_result=None):
    row_len = len(pattern[0])
    for i in range(1, row_len):
        j = 1
        while True:
            if i - j < 0 or i + j - 1 >= row_len:
                if i == original_result:
                    break
                return i
            c1 = column(pattern, i-j)
            c2 = column(pattern, i+j-1)
            if c1 != c2:
                break
            j += 1

def flip(pattern, i, j):
    c = pattern[i][j]
    if c == '.':
       pattern[i][j] = '#'
    else:
        pattern[i][j] = '.' 

def check(pattern, original_result):
    for i in range(len(pattern)):
        for j in range(len(pattern[0])):
            flip(pattern, i, j)
            result = check_vertical(pattern, original_result)
            if result and result != original_result:
                return result
            result = check_horizontal(pattern, original_result)
            if result and result != original_result:
                return result
            flip(pattern, i, j)

counter = 0
for pattern in patterns:
    original_result = check_vertical(pattern)
    if not original_result:
        original_result = check_horizontal(pattern)
    counter += check(pattern, original_result)
    
print(counter)
