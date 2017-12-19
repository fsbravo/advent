import numpy as np


def position(infile, n=1):
    moves = get_moves(infile)
    alphabet = 'abcdefghijklmnop'

    # determine shuffle and dictionary swaps
    shuffle = range(len(alphabet))
    # a_test = [c for c in alphabet]
    p_dict = {c: i for i, c in enumerate(alphabet)}
    for mv in moves:
        if mv[0] == 's':
            m = int(mv[1:]) % len(shuffle)
            shuffle = shuffle[-m:] + shuffle[:len(shuffle)-m]
        elif mv[0] == 'x':
            a, b = mv[1:].split('/')
            a, b = int(a), int(b)
            tmp = shuffle[a]
            shuffle[a] = shuffle[b]
            shuffle[b] = tmp
        elif mv[0] == 'p':
            a, b = mv[1:].split('/')
            # ia, ib = a_test.index(a), a_test.index(b)
            # tmp = a_test[ia]
            # a_test[ia] = a_test[ib]
            # a_test[ib] = tmp
            tmp = p_dict[a]
            p_dict[a] = p_dict[b]
            p_dict[b] = tmp
    d_shuffle = [p_dict[c] for c in alphabet]
    # d_shuffle = [alphabet.index(c) for c in a_test]
    # apply shuffle and dictionary swaps n times
    shuffle = np.array(shuffle)
    x = np.array(xrange(16))
    x_d = np.array(xrange(16))
    d_shuffle = np.array(d_shuffle)
    alphabet = np.array([c for c in alphabet])
    for k in xrange(n):
        x = x[shuffle]
        x_d = x_d[d_shuffle]
    p_inv = {i: c for c, i in zip(alphabet, x_d)}
    alphabet = [p_inv[i] for i in x]
    return ''.join(c for c in alphabet)


def position_slow(infile, n=1):
    moves = get_moves(infile)
    alphabet = 'abcdefghijklmnop'
    programs = [c for c in alphabet]
    for k in xrange(n):
        for mv in moves:
            if mv[0] == 's':
                programs = spin(programs, mv)
            elif mv[0] == 'x':
                programs = exchange(programs, mv)
            elif mv[0] == 'p':
                programs = partner(programs, mv)
    return ''.join(c for c in programs)


def spin(programs, mv):
    n = int(mv[1:]) % len(programs)
    return programs[-n:] + programs[:len(programs)-n]


def exchange(programs, mv):
    a, b = mv[1:].split('/')
    ia, ib = int(a), int(b)
    tmp = programs[ia]
    programs[ia] = programs[ib]
    programs[ib] = tmp
    return programs


def partner(programs, mv):
    a, b = mv[1:].split('/')
    ia, ib = programs.index(a), programs.index(b)
    tmp = programs[ia]
    programs[ia] = programs[ib]
    programs[ib] = tmp
    return programs


def get_moves(infile):
    with open(infile, 'r') as fin:
        moves = fin.read().split(',')
    return moves
