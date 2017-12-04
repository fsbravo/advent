import numpy as np


def count_valid_triangles(input):
    count = 0
    with open(input, 'r') as fin:
        for l in fin:
            values = [int(v) for v in l.split()]
            count += is_valid_triangle(values)
    return count


def is_valid_triangle(values):
    values = np.sort(values)
    return values[2] < values[0] + values[1]


def count_valid_triangles_2(input):
    count = 0
    with open(input, 'r') as fin:
        lines = []
        for l in fin:
            lines.append([int(v) for v in l.split()])
            if len(lines) == 3:
                triangles = zip(*lines)
                for t in triangles:
                    count += is_valid_triangle(t)
                lines = []
    return count