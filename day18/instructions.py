from collections import defaultdict
import Queue


class Registers(object):

    def __init__(self, rid, instructions, mode=1):
        self.instructions = instructions
        self.registers = defaultdict(int)
        self.registers['p'] = rid
        self.queue = Queue.Queue()
        self.i = 0
        self.sent = 0
        self.rid = rid
        self.mode = mode

    def get_val(self, val):
        try:
            return int(val)
        except Exception:
            return self.registers[val]

    def process_instructions(self, other_queue=None):
        moved = False
        while self.i >= 0 and self.i < len(self.instructions):
            ins = self.instructions[self.i]
            if ins[0] == 'snd':
                val = self.get_val(ins[1])
                if self.mode == 1:
                    self.sent = val
                elif self.mode == 2:
                    other_queue.put(val)
                    self.sent += 1
            elif ins[0] == 'rcv':
                if self.mode == 1:
                    return self.sent
                elif self.mode == 2:
                    if self.queue.empty():
                        break
                    val = self.queue.get()
                    self.registers[ins[1]] = val
            elif ins[0] == 'set':
                self.registers[ins[1]] = self.get_val(ins[2])
            elif ins[0] == 'add':
                self.registers[ins[1]] += self.get_val(ins[2])
            elif ins[0] == 'mul':
                self.registers[ins[1]] *= self.get_val(ins[2])
            elif ins[0] == 'mod':
                self.registers[ins[1]] %= self.get_val(ins[2])
            elif ins[0] == 'jgz':
                val = self.get_val(ins[1])
                if val > 0:
                    jump = self.get_val(ins[2])
                    self.i += jump
                    moved = True
                    continue
            self.i += 1
            moved = True
        return moved


def follow(infile):
    with open(infile, 'r') as fin:
        data = fin.read().split('\n')
        data = [d.split() for d in data]

    r_0 = Registers(0, data, mode=2)
    r_1 = Registers(1, data, mode=2)

    while True:
        check0 = r_0.process_instructions(r_1.queue)
        check1 = r_1.process_instructions(r_0.queue)
        if not check0 and not check1:
            break

    r = Registers(0, data, mode=1)
    return r.process_instructions(), r_1.sent


if __name__ == "__main__":
    answers = follow('input.txt')
    print 'Answer 1: {}'.format(answers[0])
    print 'Answer 2: {}'.format(answers[1])
