with open('day5.txt') as f:
    data = list(map(int, f.read().strip().split(',')))

#data = list(map(int, input('program> ').strip().split(',')))

opcode = 0
pc = 0
a = 0
b = 0
c = 0


def nth(num, n):
   return num // 10**(n-1) % 10


def parse_opcode(x):
    global a
    global b
    global c
    a = nth(x, 5)
    b = nth(x, 4)
    c = nth(x, 3)
    return nth(x, 2)*10 + nth(x, 1)


while opcode != 99:
    raw_opcode = data[pc]
    opcode = parse_opcode(raw_opcode)

    if opcode == 1:
        r0, r1, rx = data[pc+1], data[pc+2], data[pc+3]
        if c == 0:
            xx = data[r0]
        else:
            xx = r0

        if b == 0:
            yy = data[r1]
        else:
            yy = r1

        data[rx] = xx + yy
        pc += 4

    if opcode == 2:
        r0, r1, rx = data[pc+1], data[pc+2], data[pc+3]
        if c == 0:
            xx = data[r0]
        else:
            xx = r0

        if b == 0:
            yy = data[r1]
        else:
            yy = r1

        data[rx] = xx * yy
        pc += 4

    if opcode == 3:
        param = int(input('> '))
        data[data[pc+1]] = param
        pc += 2

    if opcode == 4:
        output = data[data[pc+1]]
        print(output)
        pc += 2

    if opcode == 5:
        r1, r2 = data[pc+1], data[pc+2]

        param1 = data[r1] if c == 0 else r1
        param2 = data[r2] if b == 0 else r2
        if param1 != 0:
            pc = param2
        else:
            pc += 3

    if opcode == 6:
        r1, r2 = data[pc+1], data[pc+2]

        param1 = data[r1] if c == 0 else r1
        param2 = data[r2] if b == 0 else r2
        if param1 == 0:
            pc = param2
        else:
            pc += 3

    if opcode == 7:
        r1, r2, r3 = data[pc+1], data[pc+2], data[pc+3]

        param1 = data[r1] if c == 0 else r1
        param2 = data[r2] if b == 0 else r2

        if param1 < param2:
            data[r3] = 1
        else:
            data[r3] = 0
        pc += 4

    if opcode == 8:
        r1, r2, r3 = data[pc+1], data[pc+2], data[pc+3]

        param1 = data[r1] if c == 0 else r1
        param2 = data[r2] if b == 0 else r2

        if param1 == param2:
            data[r3] = 1
        else:
            data[r3] = 0
        pc += 4
