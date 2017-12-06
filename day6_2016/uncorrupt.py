def uncorrupt(file):
    with open(file, 'r') as fin:
        data = fin.read()
    columns = zip(*data.split('\n'))
    result = [max(set(c), key=c.count) for c in columns]
    return ''.join(result)


def uncorrupt_2(file):
    with open(file, 'r') as fin:
        data = fin.read()
    columns = zip(*data.split('\n'))
    result = [min(set(c), key=c.count) for c in columns]
    return ''.join(result)