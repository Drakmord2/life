
# Interesting cell patterns


def shuttle():
    left_block = [(2, 8), (3, 8), (2, 9), (3, 9)]
    right_block = [(22, 8), (23, 8), (22, 9), (23, 9)]
    ship = [(7, 8), (8, 7), (8, 9), (9, 6), (9, 10), (10, 7), (10, 8), (10, 9), (11, 5), (11, 6), (11, 10), (11, 11)]

    points = left_block + right_block + ship

    return points


def glider_gun():
    pass


def glider():
    points = [(15, 13), (16, 13), (17, 13), (17, 12), (16, 11)]

    return points


def nova():
    points = [(15, 13), (16, 13), (17, 13), (16, 11)]

    return points


def die_hard():
    points = [(15, 12), (16, 12), (16, 13), (20, 13), (21, 13), (22, 13), (21, 11)]

    return points


def life():
    l = [(0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10), (0, 11), (0, 12), (0, 13), (0, 14), (0, 15), (0, 16), (0, 17),
         (0, 18), (0, 19), (1, 19), (2, 19), (3, 19), (4, 19), (5, 19), (6, 19)]

    i = [(9, 5), (10, 5), (11, 5), (12, 5), (13, 5),
         (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11), (11, 12), (11, 13), (11, 14), (11, 15), (11, 16), (11, 17),
         (11, 18), (11, 19),
         (9, 19), (10, 19), (11, 19), (12, 19), (13, 19)]

    f = [(16, 5), (17, 5), (18, 5), (19, 5), (20, 5), (21, 5), (22, 5),
         (16, 5), (16, 6), (16, 7), (16, 8), (16, 9), (16, 10), (16, 11), (16, 12), (16, 13), (16, 14), (16, 15), (16, 16), (16, 17),
         (16, 18), (16, 19),
         (16, 10), (17, 10), (18, 10), (19, 10), (20, 10), (21, 10), (22, 10)]

    e = [(25, 5), (26, 5), (27, 5), (28, 5), (29, 5),
         (25, 12), (26, 12), (27, 12), (28, 12), (29, 12),
         (25, 19), (26, 19), (27, 19), (28, 19), (29, 19),
         (25, 5), (25, 6), (25, 7), (25, 8), (25, 9), (25, 10), (25, 11), (25, 12), (25, 13), (25, 14), (25, 15), (25, 16), (25, 17),
         (25, 18), (25, 19)]

    points = l + i + f + e

    return points