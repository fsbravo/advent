import numpy as np

def position(infile, n=1):
	moves = get_moves(infile)
	alphabet = 'abcdefghijklmnop'
	programs = [c for c in alphabet]
	for mv in moves:
		if mv[0] == 's':
			programs = spin(programs, mv)
		elif mv[0] == 'x':
			programs = exchange(programs, mv)
		elif mv[0] == 'p':
			programs = partner(programs, mv)
	if n > 1:
		# find re-indexing
		indexes = np.array([alphabet.index(c) for c in programs])
		nums = np.array(range(16))
		for k in range(n):
			nums = nums[indexes]
		programs = [alphabet[i] for i in nums]
	return ''.join(c for c in programs)


def spin(programs, mv):
	n = int(mv[1:]) % len(programs)
	return programs
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
