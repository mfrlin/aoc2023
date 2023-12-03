def out_of_bounds(x, y):
    return x < 0 or y < 0 or x >= len(schematics) or y >= len(schematics[0])

def get_number(x, y):
    number = ''
    if out_of_bounds(x, y):
        return
    row = schematics[x]
    if row[y].isdigit():
        number = row[y]
    else:
        return
    # go right
    for c in row[y+1:]:
        if c.isdigit():
            number += c
        else:
            break
    # go left
    for c in row[y-1::-1]:
        if c.isdigit():
            number = c + number
        else:
            break
    if not number:
        return
    return int(number)

counter = 0
schematics = []
symbols = []
with open('input.txt') as f:
    for row_n, row in enumerate(f):
        row = row.strip()
        schematics.append(row)
        for col_n, c in enumerate(row):
            # if c not in ['.', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:  PART 1
            if c == '*':  # PART 2
                symbols.append((row_n, col_n))

for symbol in symbols:
    found_numbers = []
    # check straight above
    n = get_number(symbol[0] - 1, symbol[1])
    if not n:
        # check left above
        n = get_number(symbol[0] - 1, symbol[1] - 1)
        if n:
            # counter += n  # PART 1
            found_numbers.append(n)  # PART 2
        # check right above
        n = get_number(symbol[0] - 1, symbol[1] + 1)
        if n:
            # counter += n  # PART 1
            found_numbers.append(n)  # PART 2
    else:
        # counter += n  # PART 1
        found_numbers.append(n)  # PART 2
    # check straight below
    n = get_number(symbol[0] + 1, symbol[1])
    if not n:
        # check left below
        n = get_number(symbol[0] + 1, symbol[1] - 1)
        if n:
            # counter += n  # PART 1
            found_numbers.append(n)  # PART 2
        # check right below
        n = get_number(symbol[0] + 1, symbol[1] + 1)
        if n:
            # counter += n  # PART 1
            found_numbers.append(n)  # PART 2
    else:
        # counter += n  # PART 1
        found_numbers.append(n)  # PART 2

    # check left
    n = get_number(symbol[0], symbol[1] - 1)
    if n:
        # counter += n  # PART 1
        found_numbers.append(n)  # PART 2

    # check right
    n = get_number(symbol[0], symbol[1] + 1)
    if n:
        # counter += n  # PART 1
        found_numbers.append(n)  # PART 2

    # PART 2
    if len(found_numbers) == 2:
        counter += found_numbers[0] * found_numbers[1]

print(counter)