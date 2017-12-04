def how_many_blocks(instructions):
    instructions = [i.strip() for i in instructions.split(',')]
    moves = [(a[0], int(a[1:])) for a in instructions]

    direction = 0
    ew = 0
    ns = 0

    for d, x in moves:
        if d == 'R':
            direction = (direction + 1) % 4
        else:
            direction = (direction - 1) % 4
        ns += x * (direction == 0) - x * (direction == 2)
        ew += x * (direction == 1) - x * (direction == 3)

    return abs(ew) + abs(ns)


def how_many_blocks_2(instructions):
    instructions = [i.strip() for i in instructions.split(',')]
    moves = [(a[0], int(a[1:])) for a in instructions]

    direction = 0
    ew = 0
    ns = 0
    record = [(0, 0)]

    for d, x in moves:
        if d == 'R':
            direction = (direction + 1) % 4
        elif d == 'L':
            direction = (direction - 1) % 4
        for i in xrange(x):
            ns += 1 * (direction == 0) - 1 * (direction == 2)
            ew += 1 * (direction == 1) - 1 * (direction == 3)
            if (ew, ns) in record:
                return abs(ew) + abs(ns)
            record.append((ew, ns))