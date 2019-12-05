from collections import defaultdict
from math import copysign


with open('coords.txt') as f:
    w = [map(int, x.strip().split(',')) for x in f.readlines()]

seen = defaultdict(lambda: 0)
pos = [0, 0]
for a, b in w:
    x_sign = int(copysign(1, a-pos[0]))
    for x in range(pos[0] + x_sign, a+x_sign, x_sign):
        pair = (x, pos[1])
        seen[pair] += 1
        pos[0] = x

    y_sign = int(copysign(1, b-pos[1]))
    for y in range(pos[1] + y_sign, b+y_sign, y_sign):
        pair = (pos[0], y)
        seen[pair] += 1
        pos[1] = y

print(sum(sum(range(val + 1)) for val in seen.values()))
