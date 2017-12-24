import numpy as np


def read_components(infile):
    with open(infile, 'r') as fin:
        components = [tuple(int(v) for v in c.split('/'))
                      for c in fin.read().split('\n')]

    components = set(components)
    return components


def strongest_recursion(components, score=0, free=0):
    if len(components) == 0:
        return score
    # available options in remaining components
    options = [c for c in components if free in c]
    if len(options) == 0:
        return score
    # unused port in each component
    free = [c[0] if c[0] != free else c[1] for c in options]
    # remaining components after removing option
    comps = [components-set([c]) for c in options]
    # total score
    scores = [score + sum(c) for c in options]
    # compile subtrees
    subtrees = map(strongest_recursion, comps, scores, free)

    return max(subtrees)


def strongest_longest(components, length=0, score=0, free=0):
    if len(components) == 0:
            return score
    # available options in remaining components
    options = [c for c in components if free in c]
    if len(options) == 0:
        return length, score
    # unused port in each component
    free = [c[0] if c[0] != free else c[1] for c in options]
    # remaining components after removing option
    comps = [components-set([c]) for c in options]
    # bridge constructed (not used)
    lengths = [length + 1 for c in options]
    # total score
    scores = [score + sum(c) for c in options]
    # compile subtrees and select strongest longest bridge
    subtrees = sorted(map(strongest_longest, comps, lengths, scores, free))
    return subtrees[-1]


if __name__ == "__main__":
    components = read_components('input.txt')
    print 'Answer 1: {}'.format(strongest_recursion(components))
    a = strongest_longest(components)
    print 'Answer 2: {}'.format(a[-1])
