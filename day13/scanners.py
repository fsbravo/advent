import numpy as np


def read_layers(infile):
    layers = {}
    with open(infile, 'r') as fin:
        for l in fin:
            data = l.split(':')
            layers[int(data[0])] = int(data[1])
    return layers


def find_hit(layerno, depth, delay):
    """
    Determines if there's a hit for layer at given delay.
    """
    return (layerno + delay) % (2 * (depth - 1)) == 0


def severity(layers, delay=0):
    return sum([k * val for k, val in layers.iteritems()
                if find_hit(k, val, delay)])


def best_delay(layers):
    """
    Checks hits for each layer at each delay, stops whenever
    a zero is found (starts with lower depth layers to break
    sooner).
    """
    delay = 0
    skeys = sorted(layers.keys(), key=lambda k: layers[k])
    while True:
        okay = True
        for k in skeys:
            if find_hit(k, layers[k], delay):
                okay = False
                break
        if not okay:
            delay += 1
            continue
        break
    return delay


if __name__ == "__main__":
    layers = read_layers('input.txt')
    print 'Answer 1: {}'.format(severity(layers))
    print 'Answer 2: {}'.format(best_delay(layers))
