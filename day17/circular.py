import numpy as np


def buffer(num, n):
    pos = 0
    l = 1
    children = np.zeros(n+1, dtype=np.int32)
    for i in xrange(1, n+1):
        steps = num % l
        for k in xrange(steps):
            pos = children[pos]
        bf, nt = pos, children[pos]
        children[i] = nt
        children[bf] = i
        pos = i
        l += 1
    return nt


def buffer_2(num, n):
    pos = 0
    answer = 0
    for i in xrange(1, n+1):
        pos = (pos + num) % i
        if pos == 0:
            answer = i
        pos += 1
    return answer


if __name__ == "__main__":
    print 'Answer 1: {}'.format(buffer(345, 2017))
    print 'Answer 2: {}'.format(buffer_2(345, 50000000))
