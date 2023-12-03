import math

# PART 1
# MAX = {
#     'blue': 14,
#     'red': 12,
#     'green': 13,
# }

# def draw_valid(draw):
#     for color in draw.split(','):
#         number, color = color.strip().split(' ')
#         if int(number) > MAX[color]:
#             return False
#     return True

# counter = 0

# with open('input.txt') as f:
#     for l in f:
#         l = l.strip()
#         game_id, draws = l.split(':')
#         game_id = int(game_id[4:])
#         draws = draws.split(';')
#         for draw in draws:
#             if not draw_valid(draw):
#                 break
#         else:
#             counter += game_id

# print(counter)

# PART 2
counter = 0
with open('input.txt') as f:
    for l in f:
        l = l.strip()
        _, draws = l.split(':')
        draws = draws.split(';')
        max_colors = {'red': 0, 'blue': 0, 'green': 0}
        for draw in draws:
            for color in draw.split(','):
                number, color = color.strip().split(' ')
                if int(number) > max_colors[color]:
                    max_colors[color] = int(number)
        counter += math.prod(max_colors.values())
            

print(counter)