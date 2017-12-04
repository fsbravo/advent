import re
from collections import defaultdict


def checkrooms(inputfile):
    count = 0
    with open(inputfile, 'r') as fin:
        for l in fin:
            valid, _ = is_valid_room(l)
            count += valid
    return count


def is_valid_room(room):
    p = '(?P<letters>([a-z]+-)+)(?P<num>[0-9]+)\[(?P<checksum>[a-z]{5})\]'
    m = re.search(p, room)
    letters = m.group('letters')
    num = int(m.group('num'))
    checksum = m.group('checksum')

    counts = defaultdict(int)
    for c in letters:
        if c == '-':
            continue
        counts[c] += 1
    order = sorted([(-counts[k], k) for k in counts.keys()])
    if ''.join([t[1] for t in order[0:5]]) == checksum:
        return num, (letters, num)
    return 0, (letters, num)


def find_room(inputfile):
    rooms = []
    with open(inputfile, 'r') as fin:
        for l in fin:
            valid, room = is_valid_room(l)
            if valid:
                rooms.append(unshift_letters(*room))
                if rooms[-1][0].startswith('north'):
                    print rooms[-1]
    return rooms


def unshift_letters(letters, shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    unscrambler = {c: alphabet[(i+shift) % len(alphabet)]
                   for i, c in enumerate(alphabet)}
    unscrambler['-'] = '-'
    return ''.join(unscrambler[c] for c in letters), shift
