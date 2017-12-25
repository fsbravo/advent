import re
import numpy as np


class State(object):

    def __init__(self, tups0, tups1):
        self.write, self.move, self.nstate = {}, {}, {}
        self.write[0] = tups0[0]
        self.write[1] = tups1[0]
        self.move[0] = tups0[1]
        self.move[1] = tups1[1]
        self.nstate[0] = tups0[2]
        self.nstate[1] = tups1[2]

    def instruct(self, val):
        return self.write[val], self.move[val], self.nstate[val]


class Turing(object):

    def __init__(self, diagnostic):
        self.read_diagnostics(diagnostic)

    def run_diagnostics(self):
        for i in xrange(self.maxsteps):
            self.tape[self.pos], mv, self.cur_state = \
                self.states[self.cur_state].instruct(self.tape[self.pos])
            self.pos += mv
        return self.tape.sum()

    def read_diagnostics(self, diagnostic):
        with open(diagnostic, 'r') as fin:
            data = fin.read()

        states = re.findall('In state ([A-Z])', data)
        writes = [int(w) for w in
                  re.findall('Write the value ([0-9])', data)]
        moves = [1 if mv == 'right' else -1 for mv in
                 re.findall('Move one slot to the (right|left)', data)]
        nstates = re.findall('Continue with state ([A-Z])', data)

        tups = zip(writes, moves, nstates)
        self.states = {}
        for i, s in enumerate(states):
            self.states[s] = State(tups[2*i], tups[2*i+1])

        self.cur_state = re.findall('Begin in state ([A-Z])', data)[0]

        maxsteps = int(re.findall('after ([0-9]+) steps', data)[0])
        self.tape = np.zeros(2*maxsteps+1, dtype=np.int32)
        self.pos = maxsteps + 1
        self.maxsteps = maxsteps


if __name__ == "__main__":
    T = Turing('input.txt')
    print 'Answer 1: {}'.format(T.run_diagnostics())
    print 'End of challenge.'