def find_wins(time, distance):
    wins = 0
    for hold_time in range(1, time):
        if hold_time * (time - hold_time) > distance:
            wins += 1
    return wins

with open('input.txt') as f:
    lines = f.readlines()

# PART 1
# _, times = lines[0].split(':')
# times = [int(t) for t in times.strip().split(' ') if t]
# _, distances = lines[1].split(':')
# distances = [int(d) for d in distances.strip().split(' ') if d]
#
# counter = 1
# for t, d in zip(times, distances):
#     wins = find_wins(t, d)
#     counter *= wins

# print(counter)

# PART 2
_, time = lines[0].split(':')
time = int(time.replace(' ', '')) 
_, distance = lines[1].split(':')
distance = int(distance.replace(' ', ''))

print(time)
print(distance)

print(find_wins(time, distance))
