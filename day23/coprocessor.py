from collections import defaultdict
import Queue


class CoProcessor(object):

    def __init__(self, debug=True):
        self.instructions = {'set': self.set,
                             'sub': self.sub,
                             'mul': self.mul,
                             'jnz': self.jnz}
        self.reset(debug)

    def reset(self, debug=True):
        self.registers = {k: 0 for k in 'abcdefgh'}
        if not debug:
            self.registers['a'] = 1

    def set(self, vals):
        self.registers[vals[0]] = self.get_val(vals[1])
        return 1

    def sub(self, vals):
        self.registers[vals[0]] -= self.get_val(vals[1])
        return 1

    def mul(self, vals):
        self.registers[vals[0]] *= self.get_val(vals[1])
        return 1

    def jnz(self, vals):
        if self.get_val(vals[0]) != 0:
            return self.get_val(vals[1])
        else:
            return 1

    def get_val(self, val):
        return self.registers[val] if val in self.registers.keys() \
            else int(val)

    def read_instructions(self, infile):
        with open(infile, 'r') as fin:
            instructions = fin.read().split('\n')
            instructions = [i.split() for i in instructions]
        return instructions

    def count_target(self, infile, target='mul'):
        instructions = self.read_instructions(infile)
        i = 0
        count = 0
        while i >= 0 and i < len(instructions):
            ins = instructions[i]
            if ins[0] == target:
                count += 1
            i += self.instructions[ins[0]](ins[1:])
        return count

    def value_at_end(self, infile, target='h'):
        instructions = self.read_instructions(infile)
        i = 0
        while i >= 0 and i < len(instructions):
            ins = instructions[i]
            i += self.instructions[ins[0]](ins[1:])
        return self.registers[target]


def optimized():
    # removing loops
    b = 107900
    c = 124900

    def primes(n):
        """
        Sieve of Erastothenes
        """
        if n <= 2:
            return []
        sieve = [True]*(n+1)
        for x in xrange(3, int(n**0.5)+1, 2):
            for y in xrange(3, (n/x)+1, 2):
                sieve[x*y] = False

        return [2]+[i for i in xrange(3, n, 2) if sieve[i]]

    our_primes = primes(c/2)

    h = 0
    while True:
        f = 1
        d = 2
        # f is 0 if b divides d evenly for some d between 2 and b/2
        ps = [p for p in our_primes if p <= b/d]
        for p in ps:
            if b % p == 0:
                f = 0
                break
        if f == 0:
            h += 1
        if b == c:
            break
        b += 17
    return h


if __name__ == "__main__":
    c = CoProcessor()
    print 'Answer 1: {}'.format(c.count_target('input.txt'))
    print 'Answer 2: {}'.format(optimized())