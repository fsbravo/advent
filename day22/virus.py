import numpy as np


class Virus(object):

    def __init__(self):
        self.pos = np.array([0, 0], dtype=np.int32)
        # north, west, south, east
        self.directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        self.directions = [np.array(t, dtype=np.int32)
                           for t in self.directions]
        self.orientation = 0

    def turn_left_move(self):
        self.orientation = (self.orientation + 1) % 4
        self.pos += self.directions[self.orientation]

    def turn_right_move(self):
        self.orientation = (self.orientation - 1) % 4
        self.pos += self.directions[self.orientation]

    def go_straight_move(self):
        self.pos += self.directions[self.orientation]

    def reverse_move(self):
        self.orientation = (self.orientation + 2) % 4
        self.pos += self.directions[self.orientation]

    def initialize(self, mapfile, n=10000):
        with open(mapfile, 'r') as fin:
            mapdata = fin.read()
        maprows = mapdata.split('\n')

        def convert(c):
            return 1 if c == '#' else 0

        small = np.array([[convert(c) for c in row] for row in maprows],
                         dtype=np.int32)
        # create larger map (not too large)
        msmall = int(small.shape[0])
        m = max(int(np.sqrt(n)), msmall+10)
        if m % 2 == 0:
            m = m + 1

        large = np.zeros((m, m), dtype=np.int32)
        low = m/2 - msmall/2
        large[low:low+msmall, low:low+msmall] = small

        # change position to center
        self.pos[0] = m/2
        self.pos[1] = m/2

        return large

    def infect(self, mapfile, n=10000):
        large = self.initialize(mapfile, n)

        count = 0
        for i in xrange(n):
            if large[self.pos[0], self.pos[1]] == 1:
                large[self.pos[0], self.pos[1]] = 0
                self.turn_right_move()
            else:
                count += 1
                large[self.pos[0], self.pos[1]] = 1
                self.turn_left_move()
        return count

    def evolved_infect(self, mapfile, n=10000):
        large = self.initialize(mapfile, n)

        # 2 for weakened
        # 3 for flagged
        count = 0
        for i in xrange(n):
            # infected
            x = self.pos[0]
            y = self.pos[1]
            status = large[x, y]
            if status == 1:             # infected
                large[x, y] = 3
                self.turn_right_move()
            elif status == 0:           # clean
                large[x, y] = 2
                self.turn_left_move()
            elif status == 2:           # weakened
                count += 1
                large[x, y] = 1
                self.go_straight_move()
            elif status == 3:           # flagged
                large[x, y] = 0
                self.reverse_move()
        return count

if __name__ == "__main__":
    v = Virus()
    print 'Answer 1: {}'.format(v.infect('input.txt', n=10000))
    print 'Answer 2: {}'.format(v.evolved_infect('input.txt', n=10000000))
