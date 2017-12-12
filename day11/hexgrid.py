import numpy as np


def min_distance(filein):

    with open(filein, 'r') as fin:
        instructions = fin.read().split(',')
    instructions = [i.strip() for i in instructions]

    position = find_position(instructions)
    return find_steps(position), furthest(instructions)


def find_position(instructions, start=None):
    pos = np.zeros(2) if start is None else start

    tmp = np.cos(np.pi / 6.)
    for i in instructions:
        if i == 'n':
            pos += (0., 1.)
        elif i == 'ne':
            pos += (tmp, .5)
        elif i == 'se':
            pos += (tmp, -.5)
        elif i == 's':
            pos += (0., -1.)
        elif i == 'sw':
            pos += (-tmp, -.5)
        elif i == 'nw':
            pos += (-tmp, .5)

    return pos


def find_steps(pos):
    lateral = int(round(abs(pos[0] / np.cos(np.pi / 6.))))
    vlateral = lateral / 2.
    if vlateral > abs(pos[1]):
        return lateral
    return lateral + int(round(abs(pos[1]) - vlateral))


def furthest(instructions):
    pos = np.zeros(2)
    maxsteps = 0
    for i in instructions:
        pos = find_position([i], start=pos)
        steps = find_steps(pos)
        if steps > maxsteps:
            maxsteps = steps
    return maxsteps


if __name__ == "__main__":
    steps, furthest = min_distance('input.txt')
    print 'Answer 1: {}'.format(steps)
    print 'Answer 2: {}'.format(furthest)