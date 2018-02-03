
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
