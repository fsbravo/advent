def score(infile):
	with open(infile, 'r') as fin:
		data = fin.read()

	return calc_score(data)


def calc_score(data):
	score = 0
	depth = 0
	in_garbage = False
	i = 0
	while True and i < len(data):
		c = data[i]
		if in_garbage:
			if c == '!':
				i += 2
				continue
			if c == '>':
				in_garbage = False
		else:
			if c == '{':
				depth += 1
			elif c == '<':
				in_garbage = True
			elif c == '}':
				score += depth
				depth -= 1
		i += 1
	return score


def garbage(infile):
	with open(infile, 'r') as fin:
		data = fin.read()

	return count_garbage(data)


def count_garbage(data):
	count = 0
	depth = 0
	in_garbage = False
	i = 0
	while True and i < len(data):
		c = data[i]
		if in_garbage:
			if c == '!':
				i += 2
				continue
			if c == '>':
				in_garbage = False
				continue
			count += 1
		else:
			if c == '{':
				depth += 1
			elif c == '<':
				in_garbage = True
			elif c == '}':
				depth -= 1
		i += 1
	return count

