import math
import numpy as np


def how_many_steps(num):

    # each increasing layer is a square of size 2*i-1
    # it has (2*i-1)**2 - (# previous) elements

    length = int(math.ceil(math.sqrt(num)))
    if length % 2 == 0:
        length += 1
    layer_no = (length - 1) / 2

    # how many elements came before
    previous = (length - 2) ** 2

    # figure out pattern
    # 0 layer 0
    # 12 12 12 12 layer 1
    # 2343 2343 2343 2343 layer 2
    # 345654 345654 345654 345654 layer 3
    p_length = layer_no * 2
    pattern = range(layer_no, layer_no + p_length / 2 + 1)
    pattern += pattern[-2:-0:-1]
    pattern = pattern * 4
    # fix pattern to account for starting entry moving diagonally
    pattern = pattern[-layer_no+1:] + pattern[:-layer_no+1]

    # return position
    return pattern[num - previous - 1]


def how_many_steps_2(num):

    length = int(math.ceil(math.sqrt(num)))
    if length % 2 == 0:
        length += 1
    layer_no = (length + 1) / 2
    length += 2

    m = np.zeros((length, length))
    pos = [layer_no, layer_no]
    m[layer_no, layer_no] = 1
    m[layer_no, layer_no+1] = 1
    pos = [layer_no, layer_no+1]

    # fill in square in a brute-force way
    # change direction when element missing on the left
    direction = 0
    for l in xrange(layer_no):
        tmp = pos
        # north
        if direction == 0:
            tmp[0] -= 1
            if m[tmp[0], tmp[1]-1] < 1:
                direction += 1
        # west
        elif direction == 1:
            tmp[1] -= 1
            if m[tmp[0]+1, tmp[1]] < 1:
                direction += 1
        # south
        elif direction == 2:
            tmp[0] += 1
            if m[tmp[0], tmp[1]+1] < 1:
                direction += 1
        # east
        elif direction == 3:
            tmp[1] += 1
            if m[tmp[0]-1, tmp[1]] < 1:
                direction = 0
        m[tmp[0], tmp[1]] = np.sum(m[tmp[0]-1:tmp[0]+2, tmp[1]-1:tmp[1]+2])
        if m[tmp[0], tmp[1]] > num:
            return m[tmp[0], tmp[1]]
        pos = tmp
