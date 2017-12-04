from collections import defaultdict
import numpy as np


def count_valid(file):

    """
    Counts number of valid passphrases in input file.

    Each passphrase (line) must not contain repeated words.

    Tests:
    ok:     aa bb cc dd ee
    not ok: aa bb cc dd aa
    ok:     aa bb cc dd aaa
    """

    count = 0
    with open(file, 'r') as fin:
        for l in fin:
            count += is_valid_passphrase(l)
    return count


def is_valid_passphrase(passphrase):

    words = [w.strip() for w in passphrase.split()]
    return len(set(words)) == len(words)


def count_valid_2(file):

    """
    Counts number of valid passphrases in input file.

    Each passphrase (line) must not contain repeated words or
    words that are anagrams of each other.

    Tests:
    ok:     abcde fghij
    not ok: abcde xyz ecdab
    ok:     a ab abc abd abf abj
    ok:     iiii oiii ooii oooi oooo
    not ok: oiii ioii iioi iiio
    """

    count = 0
    with open(file, 'r') as fin:
        for l in fin:
            count += is_valid_passphrase_2(l)
    return count


def is_valid_passphrase_2(passphrase):

    words = [w.strip() for w in passphrase.split()]
    for i, w1 in enumerate(words):
        for w2 in words[i+1:]:
            if is_anagram(w1, w2):
                return False
    return True


def is_anagram(w1, w2):

    """
    Checks if two words are anagrams of each other.
    """

    if len(w1) != len(w2):
        return False
    d = defaultdict(int)
    for c1, c2, in zip(w1, w2):
        d[c1] += 1
        d[c2] -= 1
    return not np.any([v != 0 for v in d.values()])
