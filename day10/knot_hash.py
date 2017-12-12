def twist(input):
    data = [int(i) for i in input.split(',')]
    pos = 0
    seq = range(256)
    for skip, length in enumerate(data):
        if length > 256:
            continue
        end = (pos + length) % 256
        if end < pos:
            tmp = seq[pos:] + seq[:end]
            tmp = tmp[::-1]
            n = len(seq[pos:])
            seq[pos:] = tmp[:n]
            seq[:end] = tmp[n:]
        else:
            tmp = seq[pos:end]
            seq[pos:end] = tmp[::-1]
        pos = (pos + length + skip) % 256
    return seq[0] * seq[1]


def twist_2(input):
    data = [ord(i) for i in input.strip()]
    data += [17, 31, 73, 47, 23]
    pos = 0
    skip = 0
    seq = range(256)
    for i in range(64):
        for length in data:
            end = (pos + length) % 256
            if end < pos:
                tmp = seq[pos:] + seq[:end]
                tmp = tmp[::-1]
                n = len(seq[pos:])
                seq[pos:] = tmp[:n]
                seq[:end] = tmp[n:]
            else:
                tmp = seq[pos:end]
                seq[pos:end] = tmp[::-1]
            pos = (pos + length + skip) % 256
            skip += 1

    dense = []
    for start in range(0, 255, 16):
        dense.append(eval(' ^ '.join(str(i) for i in seq[start:start+16])))

    final = [hex(i) for i in dense]

    for i, s in enumerate(final):
        if len(s) == 3:
            final[i] = '0' + s[-1]
        else:
            final[i] = s[-2:]

    return ''.join(final)


if __name__ == "__main__":
    data = '165,1,255,31,87,52,24,113,0,91,148,254,158,2,73,153'
    print 'Answer 1: {}'.format(twist(data))
    print 'Answer 2: {}'.format(twist_2(data))
