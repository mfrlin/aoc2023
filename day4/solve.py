# PART 1
# counter = 0
# with open('input.txt') as f:
#     for row in f:
#         a_set = set()
#         b_set = set()
#         row = row.strip()
#         _, row = row.split(':')
#         a_part, b_part = row.split('|')
#         for a in a_part.strip().split(' '):
#             if a:
#                 a_set.add(int(a))
#         for b in b_part.strip().split(' '):
#             if b:
#                 b_set.add(int(b))
#         matches = len(a_set & b_set)
#         if matches:
#             counter += 2**(matches - 1) 

# print(counter)


PROCESSED = []
with open('input.txt') as f:
    for row in f:
        a_set = set()
        b_set = set()
        row = row.strip()
        _, row = row.split(':')
        a_part, b_part = row.split('|')
        for a in a_part.strip().split(' '):
            if a:
                a_set.add(int(a))
        for b in b_part.strip().split(' '):
            if b:
                b_set.add(int(b))
        matches = len(a_set & b_set)
        PROCESSED.append(matches)

copies = [1] * len(PROCESSED)
for i, n in enumerate(PROCESSED):
    increase = copies[i]
    for j in range(i+1, i + n + 1):
        copies[j] += increase

print(sum(copies))