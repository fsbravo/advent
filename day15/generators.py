def gen(start, factor, mult=None, n=40000000):
    for i in xrange(n):
        start = (start * factor) % 2147483647
        if mult:
            while start % mult != 0:
                start = (start * factor) % 2147483647
        yield start


def count_matches(start, mult=(None, None), n=40000000):
    gen_a = gen(start[0], 16807, mult[0], n)
    gen_b = gen(start[1], 48271, mult[1], n)
    count = 0
    for a, b in zip(gen_a, gen_b):
        ba = format(a, '16b')
        bb = format(b, '16b')
        count += ba[-16:] == bb[-16:]
    return count


if __name__ == "__main__":
    print 'Answer 1: {}'.format(count_matches((873, 583),
                                              40000000))
    print 'Answer 2: {}'.format(count_matches((873, 583),
                                              (4, 8),
                                              5000000))
