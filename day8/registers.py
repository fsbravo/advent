import numpy as np
from collections import defaultdict


def follow_instructions(filein):
	instructions = []
	registers = defaultdict(int)
	with open(filein, 'r') as fin:
		for l in fin:
			vals = l.split()
			name, inst, amount, _, rcond, comp, limit = vals
			sign = 1 if inst == 'inc' else -1
			registers[name] += sign*int(amount) if \
				test_cond(registers, rcond, comp, limit) else 0
	return np.max(registers.values())


def test_cond(registers, rcond, comp, limit):
	test = "registers['"+rcond+"']"+comp+str(limit)
	return eval(test)


def follow_instructions_2(filein):
	instructions = []
	registers = defaultdict(int)
	maxval = 0
	with open(filein, 'r') as fin:
		for l in fin:
			vals = l.split()
			name, inst, amount, _, rcond, comp, limit = vals
			sign = 1 if inst == 'inc' else -1
			registers[name] += sign*int(amount) if \
				test_cond(registers, rcond, comp, limit) else 0
			if registers[name] > maxval:
				maxval = registers[name]
	return maxval