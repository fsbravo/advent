import numpy as np
import re


class Recursor(object):

    def __init__(self, infile):
        self.initialize_patterns(infile)

    def initialize_patterns(self, infile):
        self.patterns = {}
        with open(infile, 'r') as fin:
            for l in fin:
                rule = re.findall('/?([#.]+)/?', l)
                sz = len(rule[0])
                k = np.array([[c for c in r] for r in rule if len(r) == sz])
                v = np.array([[c for c in r] for r in rule if len(r) > sz])
                for j in xrange(4):
                    nk = np.rot90(k, j)
                    self.patterns[self.to_str(nk)] = self.to_str(v)
                    nk = np.fliplr(nk)
                    self.patterns[self.to_str(nk)] = self.to_str(v)
                    nk = np.flipud(np.fliplr(nk))
                    self.patterns[self.to_str(nk)] = self.to_str(v)

    def to_str(self, array):
        return ''.join(array.flatten())

    def to_array(self, num):
        n = int(np.rint(np.sqrt(len(num))))
        array = np.reshape([i for i in num], (n, n))
        return array

    def expand(self, seed='.#...####', n=5):
        matrix = self.to_array(seed)
        for k in xrange(n):
            m = matrix.shape[0]
            if m % 2 == 0:
                end = m/2
                nm = m * 3 / 2
                p = 3
                s = 2
            else:
                end = m/3
                nm = m * 4 / 3
                p = 4
                s = 3
            nmatrix = np.zeros((nm, nm), dtype='|S1')
            for i in xrange(0, end):
                for j in xrange(0, end):
                    sub = matrix[i*s:(i+1)*s, j*s:(j+1)*s]
                    nsub = self.to_array(self.patterns[self.to_str(sub)])
                    nmatrix[i*p:(i+1)*p, j*p:(j+1)*p] = nsub
            matrix = nmatrix
        return matrix

    def count_on(self, seed='.#...####', n=5):
        matrix = self.expand(seed, n)
        return np.sum(matrix == '#')

if __name__ == "__main__":
    rec = Recursor('input.txt')
    print 'Answer 1: {}'.format(rec.count_on(n=5))
    print 'Answer 2: {}'.format(rec.count_on(n=18))
