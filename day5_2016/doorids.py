import hashlib


def find_password(doorid):
    password = ''
    i = 0
    while len(password) < 8:
        m = hashlib.md5()
        m.update(doorid + str(i))
        r = m.hexdigest()
        if r.startswith('00000'):
            password += str(r[5])
        i += 1
    return password


def find_password_2(doorid):
    pdict = {}
    i = -1
    while len(pdict.keys()) < 8:
        i += 1
        m = hashlib.md5()
        m.update(doorid + str(i))
        r = m.hexdigest()
        if r.startswith('00000'):
            try:
                position = int(r[5])
            except ValueError:
                continue
            if position > 7:
                continue
            if position in pdict.keys():
                continue
            pdict[position] = r[6]
    password = [None for i in xrange(8)]
    for i in pdict.keys():
        password[i] = pdict[i]
    return ''.join(password)
