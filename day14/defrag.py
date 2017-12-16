from knot_hash import *
import numpy as np
from Queue import Queue


def defrag(keystring):
    hashes = []
    for i in xrange(128):
        tmp = twist_2(keystring + '-' + str(i))
        hashes.append(hex_to_bin(tmp))
    return hashes


def count_used(keystring):
    hashes = defrag(keystring)
    count = 0
    for h in hashes:
        count += sum([1 for c in h if c == '1'])
    return count


def hex_to_bin(entry):
    return ''.join([format(int(c, 16), '04b') for c in entry])


def count_regions(keystring):
    hashes = defrag(keystring)
    regions = []
    for i, h in enumerate(hashes):
        for j, c in enumerate(h):
            if c == '1':
                regions.append((i, j))
    print len(regions)
    return len(merge(regions))


def merge(used):
    """
    Finds adjacent regions by merging through breadth-first search.
    """
    merged = []     # set of assembled regions
    open_set = Queue()  # set of explore nodes

    while len(used) > 0:    # run through disjoint components
        cur_region = []     # region in exploration
        open_set.put(used[0])
        while not open_set.empty():    # run through current region
            pos = open_set.get()
            cur_region.append(pos)
            adj = adjacent(pos[0], pos[1])
            # for each node in adjacency, if not visited and
            # also in use, add to explore set
            for tup in adj:
                if tup in cur_region:   # if we've seen it
                    continue
                if tup not in used:     # if not in use
                    continue
                open_set.put(tup)
        # once we've explore connected component
        merged.append(cur_region)
        # update regions to remove members of merged component
        used = [r for r in used if r not in cur_region]

    return merged


def adjacent(i, j, n=128):
    adjacent = [(ii, jj) for ii, jj in
                zip((i-1, i+1, i, i), (j, j, j-1, j+1)) if
                ii >= 0 and ii < n and jj >= 0 and jj < n]
    return adjacent


if __name__ == "__main__":
    keystring = 'oundnydw'
    print 'Answer 1: {}'.format(count_used(keystring))