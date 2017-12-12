import numpy as np


def find_loop(blocks):
    blocks = [int(b) for b in blocks.split()]
    memory = [tuple(blocks)]
    i = 0
    nblocks = []
    while True:
        i += 1
        nblocks = redistribute(blocks)
        if tuple(nblocks) in memory:
            break
        memory.append(tuple(nblocks))
        blocks = nblocks
    return i


def redistribute(blocks):
    i = np.argmax(blocks)
    nb = blocks[i]
    blocks[i] = 0
    n = len(blocks)
    while nb > 0:
        i = (i+1) % n
        blocks[i] += 1
        nb -= 1
    return blocks


def find_loop_2(blocks):
    blocks = [int(b) for b in blocks.split()]
    memory = [tuple(blocks)]
    i = 0
    nblocks = []
    while True:
        i += 1
        nblocks = redistribute(blocks)
        if tuple(nblocks) in memory:
            break
        memory.append(tuple(nblocks))
        blocks = nblocks
    test = tuple(nblocks)
    for j in xrange(len(memory)):
        if test == memory[j]:
            break
    return i - j


if __name__ == "__main__":
    with open('input.txt', 'r') as fin:
        data = fin.read()
    print 'Answer 1 {}'.format(find_loop(data))
    print 'Answer 2 {}'.format(find_loop_2(data))
