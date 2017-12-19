import numpy as np
import string


class Tracker(object):

    def __init__(self, data):
        self.directions = {1: (-1, 0),      # NORTH
                           -1: (1, 0),      # SOUTH
                           2: (0, 1),       # EAST
                           -2: (0, -1)}     # WEST
        self.d = -1
        self.map = data
        self.pos = np.zeros(2, dtype=np.int32)
        self.pos[1] = self.map[0].index('|')
        self.letters = []
        self.dims = np.array([len(data), np.max([len(d) for d in data])])
        self.valid = string.ascii_lowercase + string.ascii_uppercase + '+-|'
        self.chars = string.ascii_lowercase + string.ascii_uppercase
        self.steps = 1

    def find_next(self):
        # test current direction
        pos = self.test_position(self.d)
        # if current direction doesn't work, find alternative
        if pos is None:
            # skip current or reverse direction
            for d in self.directions.keys():
                if d == -self.d or d == self.d:
                    continue
                pos = self.test_position(d)
                if pos is not None:
                    self.d = d
                    self.pos = pos
                    break
        else:
            self.pos = pos
        if pos is None:
            return False
        char = self.map[self.pos[0]][self.pos[1]]
        if char in self.chars:
            self.letters.append(char)
        return True

    def test_position(self, d):
        pos = self.pos + self.directions[d]
        if np.any(pos >= self.dims) or np.any(pos < 0):
            return None
        return pos if self.map[pos[0]][pos[1]] in self.valid else None

    def follow(self):
        while self.find_next():
            self.steps += 1
        return ''.join(self.letters), self.steps


def follow_map(mapfile):
    with open(mapfile, 'r') as fin:
        data = fin.read().split('\n')

    tracker = Tracker(data)
    return tracker.follow()


if __name__ == "__main__":
    answers = follow_map('input.txt')
    print 'Answer 1: {}'.format(answers[0])
    print 'Answer 2: {}'.format(answers[1])
