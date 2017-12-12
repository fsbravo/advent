import numpy as np


def checksum(input):

    """
    Solve puzzle 1 in day 2 of advent of code 2017.

    Given a table of integers (as a string) add up the difference
    between the maximum and minimum values of each row.

    E.g.
    5 1 9 5 = 8
    7 5 3   = 4
    2 4 6 8 = 6
    total = 8 + 4 + 6 = 18
    """

    lines = input.split('\n')
    total = 0
    for l in lines:
        vals = [int(i) for i in l.split()]
        total += np.max(vals) - np.min(vals)
    return total


def checksum_2(input):

    """
    Solve puzzle 2 in day 2 of advent of code 2017.

    Given a table of integers (as a string) add up the only integer
    division for each row.

    E.g.
    5 9 2 8 = 4 (8/2)
    9 4 7 3 = 3 (9/3)
    3 8 6 5 = 2 (6/3)
    total = 4 + 3 + 2 = 9
    """

    lines = input.split('\n')
    total = np.sum(line_check(l) for l in lines)
    return total


def line_check(l):

    """
    Inefficient (but accurate) way of finding first and only
    integer division on each line.
    """

    vals = [int(i) for i in l.split()]
    for i, v1 in enumerate(vals):
        for j, v2 in enumerate(vals):
            if i == j:
                continue
            if v1 % v2 == 0:
                return v1/v2


if __name__ == "__main__":
    with open('input.txt', 'r') as fin:
        data = fin.read()
    print 'Answer 1: {}'.format(checksum(data))
    print 'Answer 2: {}'.format(checksum_2(data))
