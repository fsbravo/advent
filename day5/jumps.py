def jump(instructions):
    with open(instructions, 'r') as fin:
        test = fin.read()
    jumps = [int(i) for i in test.split('\n')]
    return count_jumps(jumps)


def count_jumps(jumps):
    n = len(jumps)
    i = 0
    pos = 0
    while pos >= 0 and pos < n:
        jumps, pos = update_position(jumps, pos)
        i += 1
    return i


def update_position(jumps, pos):
    mv = jumps[pos]
    jumps[pos] += 1
    pos += mv
    return jumps, pos


def jump_2(instructions):
    with open(instructions, 'r') as fin:
        test = fin.read()
    jumps = [int(i) for i in test.split('\n')]
    return count_jumps_2(jumps)


def count_jumps_2(jumps):
    n = len(jumps)
    i = 0
    pos = 0
    while pos >= 0 and pos < n:
        jumps, pos = update_position_2(jumps, pos)
        i += 1
    return i


def update_position_2(jumps, pos):
    mv = jumps[pos]
    if mv >= 3:
        jumps[pos] -= 1
    else:
        jumps[pos] += 1
    pos += mv
    return jumps, pos
