from aco import aco, fill_dis_matr, MAX_DIS, MIN_DIS
import numpy as np
from itertools import product
import time

m = 5  # amount of ants and cities
Q = (MIN_DIS * m, MAX_DIS * m)  # coefficient of the alleged best way

def test(d):
    good_answers = ([0, 4, 1, 3, 2], 26), ([3, 4, 0, 1, 2], 26), \
                   ([2, 0, 4, 1, 3], 26), ([2, 3, 4, 1, 0], 26), \
                   ([1, 4, 0, 2, 3], 26), ([0, 4, 3, 2, 1], 26)

    e = (0, 1, 2, 3)  # amount of elite ants

    a = (1, 2, 3)  # coefficient of strengthen the sense of smell
    b = (1, 2, 3)  # coefficient of strengthen of desire

    t_max = (100, 200, 300, 400, 500)  # the amount of "generations"
    p = (0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7)  # coefficient of evaporation

    best_time = None
    best_set = None
    best_q = None

    for t in t_max:
        for q in Q:
            for s in product(e, a, b, p):
                st = time.clock()
                res = aco(m, s[0], d, t, s[1], s[2], s[3], q)
                en = time.clock() - st
                # print(s)
                if res in good_answers:
                    if best_time is None or en < best_time:
                        best_time = en
                        best_set = s
                        best_q = q

        print("For {} generations with {} approx best time is {} witn set of parameters {}".format(
            t, best_q, best_time, best_set
        ))

        best_time = None
        best_set = None
        best_q = None





if __name__ == "__main__":
    d_fix = np.array([[0,   6,   3,   7,   1],
             [6,   0,   8,  10,   6],
             [3,   8,   0,   6,   7],
             [7,  10,   6,   0,   5],
             [1,   6,   7,   5,   0]])

    print(d_fix)
    test(d_fix)
