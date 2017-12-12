import re
from collections import defaultdict


def count_group(filein, gid):
    blocks = get_blocks(filein)
    group = assemble_group(blocks, gid)
    return len(group)


def assemble_group(blocks, gid):
    n = 0
    while len(blocks[gid]) != n:
        n = len(blocks[gid])
        for i in blocks[gid]:
            blocks[gid] = blocks[gid].union(blocks[i])
    return tuple(sorted(list(blocks[gid])))


def get_blocks(filein):
    blocks = defaultdict(set)
    with open(filein, 'r') as fin:
        for l in fin:
            nums = [int(r) for r in re.findall('\d+', l)]
            blocks[nums[0]] = blocks[nums[0]].union(nums[1:])
    return blocks


def count_all_groups(filein):
    blocks = get_blocks(filein)
    groups = set([assemble_group(blocks, i) for i in blocks.keys()])
    return len(groups)


if __name__ == "__main__":
    print 'Answer 1: {}'.format(count_group('input.txt', 0))
    print 'Answer 2: {}'.format(count_all_groups('input.txt'))