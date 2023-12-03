# PART 1
# def find_number(line):
#     first_digit = None
#     second_digit = None
#     for i in range(len(line)):
#         if first_digit is None and line[i].isdigit():
#             first_digit = line[i]
#         reverse_index = -(i + 1)
#         if second_digit is None and line[reverse_index].isdigit():
#             second_digit = line[reverse_index]
#         if first_digit and second_digit:
#             break
#     return int(first_digit + second_digit)

# counter = 0

# with open('input1.txt') as f:
#     for l in f:
#         counter += find_number(l)
# 
# print(counter)

# PART 2
RESULT_MAP = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}
MAP = {}
REVERSE_MAP = {}
for k in RESULT_MAP:
    inner = MAP
    reverse_inner = REVERSE_MAP
    for c, rc in zip(k, k[::-1]):
        if c not in inner:
            inner[c] = {}
        if rc not in reverse_inner:
            reverse_inner[rc] = {}
        inner = inner[c]
        reverse_inner = reverse_inner[rc]


def create_searcher(search):
    key = ''
    while True:
        c = yield
        if c.isdigit():
            return c
        key += c
        search = search.get(c)
        if search is None:
            return None
        if search == {}:
            return key


def find_number2(line):
    first_digit = None
    second_digit = None
    searchers = []
    reverse_searchers = []
    for i in range(len(line)):
        if first_digit is None:
            s = create_searcher(MAP)
            next(s)
            searchers.append(s)
            for_removal = []
            for j, searcher in enumerate(searchers):
                try:
                    searcher.send(line[i])
                except StopIteration as e:
                    if e.value:
                        first_digit = RESULT_MAP.get(e.value, e.value)
                        break
                    for_removal.append(searcher)
            for s in for_removal:
                searchers.remove(s)

        if second_digit is None:
            reverse_index = -(i + 1)
            s = create_searcher(REVERSE_MAP)
            next(s)
            reverse_searchers.append(s)
            for_removal = []
            for searcher in reverse_searchers:
                try:
                    searcher.send(line[reverse_index])
                except StopIteration as e:
                    if e.value:
                        second_digit = RESULT_MAP.get(e.value[::-1], e.value)
                        break
                    for_removal.append(searcher)
            for s in for_removal:
                reverse_searchers.remove(s)

        if first_digit and second_digit:
            break

    return int(first_digit + second_digit)

counter = 0

with open('input1.txt') as f:
    for l in f:
        counter += find_number2(l)
        

print(counter)

