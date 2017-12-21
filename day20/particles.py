import re
import numpy as np
from scipy.spatial.distance import cdist
from collections import defaultdict


def closest(particles):
    """
    Position of particle at time k is given by

    x(k) = x(0) + k*v(0) + k*(k+1)/2 * a

    We wish to find x(k) that is smallest as k->infty.
    Only the quadratic term matters in the long term, so
    we compute the term with the largest acceleration.
    """
    accs = np.abs(np.stack([p[2] for p in particles]))
    return np.argmin(accs.sum(axis=1))


def survivors(particles):
    """
    A collision happens if system below has a solution for k >= 0

    (k*k) * (ax-ay)/2 + k * (vx-vy+1/2*(ax-ay)) + x-y+2(ax-ay) = 0

    Solving quadratic equations will give non-integer value k, so we have
    to be careful in checking.
    """
    n = len(particles)
    ctimes = defaultdict(list)
    for i in xrange(n):
        for j in xrange(i+1, n):
            sols = solve_collision(particles[i], particles[j])
            for k in sols:
                ctimes[k].append((i, j))

    # process deaths in order
    dead = set()
    for k in sorted(ctimes.keys()):
        tmpdead = set()
        for tup in ctimes[k]:
            if tup[0] in dead or tup[1] in dead:
                continue
            tmpdead.add(tup[0])
            tmpdead.add(tup[1])
        # if we want to know which die
        # print k, ':', ' '.join([str(i) for i in tmpdead])
        dead = dead.union(tmpdead)

    return len(particles) - len(dead)


def solve_collision(pi, pj):
    pdiff = pi[0]-pj[0]
    vdiff = pi[1]-pj[1]
    adiff = pi[2]-pj[2]
    a, b, c = adiff/2., vdiff + adiff/2., pdiff
    ks = []
    # check if a is zero (if so we solve linear system instead)
    if np.any(a == 0):
        btmp = b[a == 0]
        ctmp = c[a == 0]
        # if linear term is zero, constant term must also be zero
        if np.any(btmp == 0):
            if np.any(ctmp[btmp == 0] != 0):
                return []
        for bt, ct in zip(btmp[btmp != 0], ctmp[btmp != 0]):
            ks.append(-ct / float(bt))
    mask = a != 0
    a = a[mask]
    b = b[mask]
    c = c[mask]
    # solution must be real
    rad = b**2-4*a*c
    if np.any(rad < -1.e-15):
        if np.all(rad > -1.e-15):
            rad = 0
        else:
            return []
    radsqrt = np.sqrt(rad)
    # find all integer possibilities
    valid = int_sols(a, b, radsqrt, ks)

    # double check that position is accurate at time k
    for k in valid:
        posx = a * k**2 + b * k + c
        if np.all(np.abs(posx) > 1.e-15):
            raise ValueError
    return valid


def int_sols(a, b, radsqrt, ks):
    # first ensure solutions from linear system are integer
    int_ks = []
    for k in ks:
        int_k = int(np.rint(k))
        if abs(int_k - k) > 1.e-16:
            return []
        int_ks.append(int_k)
    # each entry in dims corresponds to integer possibilities
    # for that dimension
    dims = [[k] for k in int_ks]
    for aa, bb, rr in zip(a, b, radsqrt):
        candidates = ((-bb-rr)/2./aa, (-bb+rr)/2./aa)
        cur = []
        for k in candidates:
            k_int = int(k)
            if abs(k_int-k) > 1.e-12:
                continue
            cur.append(k_int)
        dims.append(cur)
    sols = []
    # keep only solutions which are the same across all dimensions
    for k1 in dims[0]:
        for k2 in dims[1]:
            for k3 in dims[2]:
                if k1 == k2 and k1 == k3:
                    sols.append(k1)
    return sols


# brute-force solution (n=100 probably suffices)

def simulate_n(particles, n=1000):
    def positions(x, v, a, k):
        return x + k*v + k*(k+1)/2*a

    for i in xrange(n):
        x = np.stack([p[0] for p in particles])
        v = np.stack([p[1] for p in particles])
        a = np.stack([p[2] for p in particles])
        pos = positions(x, v, a, i)
        d = cdist(pos, pos) + np.eye(pos.shape[0])
        iii, _ = np.where(d < 1.e-10)
        iii = set(iii)
        particles = [p for i, p in enumerate(particles) if i not in iii]

    return len(particles)


def read_particles(infile):
    particles = []
    with open(infile, 'r') as fin:
        for l in fin:
            data = re.findall('-?[0-9]+', l)
            pos = np.array([int(v) for v in data[0:3]], dtype=np.int32)
            vel = np.array([int(v) for v in data[3:6]], dtype=np.int32)
            acc = np.array([int(v) for v in data[6:]], dtype=np.int32)
            particles.append([pos, vel, acc])
    return particles


if __name__ == "__main__":
    particles = read_particles('input.txt')
    print 'Answer 1: {}'.format(closest(particles))
    print 'Answer 2: {}'.format(survivors(particles))