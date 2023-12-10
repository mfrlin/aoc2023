with open('input.txt') as f:
    lines = f.readlines()


predictions = []
for line in lines:
    line = line.strip()
    # sequence = list(map(int, line.split(' ')))  # PART 1
    sequence = list(map(int, line.split(' ')))[::-1]  # PART 2
    levels = []
    levels.append(sequence)
    while True:
        level = []
        for first, second in zip(sequence, sequence[1:]):
            difference = second - first
            level.append(difference)
        levels.insert(0, level)
        if all(n == 0 for n in level):
            break
        else:
            sequence = level
    previous = 0
    for level in levels:
        y = level[-1]
        x = y + previous
        previous = x

    predictions.append(previous)

print(sum(predictions))
