from aco import aco, fill_dis_matr, MAX_DIS, MIN_DIS
import numpy as np
from itertools import product
import time
import matplotlib.pyplot as plt
import os


TIMES = 30


def test_fix_Q():
    D = np.array([[0, 6, 3, 7, 1],
                      [6, 0, 8, 10, 6],
                      [3, 8, 0, 6, 7],
                      [7, 10, 6, 0, 5],
                      [1, 6, 7, 5, 0]])

    good_answers = ([0, 4, 1, 3, 2], 26), ([3, 4, 0, 1, 2], 26), \
                   ([2, 0, 4, 1, 3], 26), ([2, 3, 4, 1, 0], 26), \
                   ([1, 4, 0, 2, 3], 26), ([0, 4, 3, 2, 1], 26)

    m = 5  # amount of ants and cities
    Q = range(MIN_DIS, MAX_DIS * m)  # coefficient of the alleged best way
    timing = [None for i in range(len(Q))]
    l = []

    p = 0.2  # coefficient of evaporation
    a = 1  # coefficient of strengthen the sense of smell
    b = 1  # coefficient of strengthen of desire
    e = 1  # amount of elite ants

    gen = 200

    for j in (0, 1, 2):
        for t in range(TIMES):
            for q in Q:
                st = time.clock()
                res = aco(m, e, D, gen, a, b, p, q)
                en = time.clock() - st
                if res in good_answers:
                    if timing[Q.index(q)] is None or en < timing[Q.index(q)]:
                        timing[Q.index(q)] = en

            print(timing)
        l.append(timing)
        timing = [None for i in range(len(Q))]

    plt.plot(Q, l[0], Q, l[1], Q, l[2])
    plt.xlabel(r'$Q$')
    plt.ylabel(r'$Time(sec)$')
    plt.title(r'Вариация параметра Q')
    plt.grid(True)
    plt.show()


def test_fix_e():
    D = np.array([[0, 6, 3, 7, 1],
                      [6, 0, 8, 10, 6],
                      [3, 8, 0, 6, 7],
                      [7, 10, 6, 0, 5],
                      [1, 6, 7, 5, 0]])

    good_answers = ([0, 4, 1, 3, 2], 26), ([3, 4, 0, 1, 2], 26), \
                   ([2, 0, 4, 1, 3], 26), ([2, 3, 4, 1, 0], 26), \
                   ([1, 4, 0, 2, 3], 26), ([0, 4, 3, 2, 1], 26)

    m = 5  # amount of ants and cities
    Q = MAX_DIS * m // 2  # coefficient of the alleged best way

    p = 0.5  # coefficient of evaporation
    a = 2  # coefficient of strengthen the sense of smell
    b = 1  # coefficient of strengthen of desire
    E = (0, 1, 2, 3, 4, 5)  # amount of elite ants

    gen = 200
    timing = [None for i in range(len(E))]
    l = []

    for j in (0, 1, 2):
        for t in range(TIMES):
            for e in E:
                st = time.clock()
                res = aco(m, e, D, gen, a, b, p, Q)
                en = time.clock() - st
                if res in good_answers:
                    if timing[E.index(e)] is None or en < timing[E.index(e)]:
                        timing[E.index(e)] = en

            print(timing)
        l.append(timing)
        timing = [None for i in range(len(E))]

    plt.plot(E, l[0], E, l[1], E, l[2])
    plt.xlabel(r'$e$')
    plt.ylabel(r'$Time(sec)$')
    plt.title(r'Вариация параметра e')
    plt.grid(True)
    plt.show()


def test_fix_a():
    D = np.array([[0, 6, 3, 7, 1],
                      [6, 0, 8, 10, 6],
                      [3, 8, 0, 6, 7],
                      [7, 10, 6, 0, 5],
                      [1, 6, 7, 5, 0]])

    good_answers = ([0, 4, 1, 3, 2], 26), ([3, 4, 0, 1, 2], 26), \
                   ([2, 0, 4, 1, 3], 26), ([2, 3, 4, 1, 0], 26), \
                   ([1, 4, 0, 2, 3], 26), ([0, 4, 3, 2, 1], 26)

    m = 5  # amount of ants and cities
    Q = MAX_DIS * m // 2  # coefficient of the alleged best way

    p = 0.5  # coefficient of evaporation
    A = (0, 1, 2, 3, 4, 5) # coefficient of strengthen the sense of smell
    b = 1  # coefficient of strengthen of desire
    e = 2  # amount of elite ants

    gen = 200
    timing = [None for i in range(len(A))]
    l = []

    for j in (0, 1, 2):
        for t in range(TIMES):
            for a in A:
                st = time.clock()
                res = aco(m, e, D, gen, a, b, p, Q)
                en = time.clock() - st
                if res in good_answers:
                    if timing[A.index(a)] is None or en < timing[A.index(a)]:
                        timing[A.index(a)] = en

            print(timing)
        l.append(timing)
        timing = [None for i in range(len(A))]

    plt.plot(A, l[0], A, l[1], A, l[2])
    plt.xlabel(r'$a$')
    plt.ylabel(r'$Time(sec)$')
    plt.title(r'Вариация параметра a')
    plt.grid(True)
    plt.show()


def test_fix_b():
    D = np.array([[0, 6, 3, 7, 1],
                  [6, 0, 8, 10, 6],
                  [3, 8, 0, 6, 7],
                  [7, 10, 6, 0, 5],
                  [1, 6, 7, 5, 0]])

    good_answers = ([0, 4, 1, 3, 2], 26), ([3, 4, 0, 1, 2], 26), \
                   ([2, 0, 4, 1, 3], 26), ([2, 3, 4, 1, 0], 26), \
                   ([1, 4, 0, 2, 3], 26), ([0, 4, 3, 2, 1], 26)

    m = 5  # amount of ants and cities
    Q = MAX_DIS * m // 2  # coefficient of the alleged best way

    p = 0.5  # coefficient of evaporation
    a = 2  # coefficient of strengthen the sense of smell
    B = (0, 1, 2, 3, 4, 5)  # coefficient of strengthen of desire
    e = 2  # amount of elite ants

    gen = 200
    timing = [None for i in range(len(B))]
    l = []

    for j in (0, 1, 2):
        for t in range(TIMES):
            for b in B:
                st = time.clock()
                res = aco(m, e, D, gen, a, b, p, Q)
                en = time.clock() - st
                if res in good_answers:
                    if timing[B.index(b)] is None or en < timing[B.index(b)]:
                        timing[B.index(b)] = en

            print(timing)
        l.append(timing)
        timing = [None for i in range(len(B))]

    plt.plot(B, l[0], B, l[1], B, l[2])
    plt.xlabel(r'$b$')
    plt.ylabel(r'$Time(sec)$')
    plt.title(r'Вариация параметра b')
    plt.grid(True)
    plt.show()


def test_fix_p():
    D = np.array([[0, 6, 3, 7, 1],
                  [6, 0, 8, 10, 6],
                  [3, 8, 0, 6, 7],
                  [7, 10, 6, 0, 5],
                  [1, 6, 7, 5, 0]])

    good_answers = ([0, 4, 1, 3, 2], 26), ([3, 4, 0, 1, 2], 26), \
                   ([2, 0, 4, 1, 3], 26), ([2, 3, 4, 1, 0], 26), \
                   ([1, 4, 0, 2, 3], 26), ([0, 4, 3, 2, 1], 26)

    m = 5  # amount of ants and cities
    Q = MAX_DIS * m // 2  # coefficient of the alleged best way

    P = (0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9)   # coefficient of evaporation
    a = 2  # coefficient of strengthen the sense of smell
    b = 1  # coefficient of strengthen of desire
    e = 2  # amount of elite ants

    gen = 200
    timing = [None for i in range(len(P))]
    l = []

    for j in (0, 1, 2):
        for t in range(TIMES):
            for p in P:
                st = time.clock()
                res = aco(m, e, D, gen, a, b, p, Q)
                en = time.clock() - st
                if res in good_answers:
                    if timing[P.index(p)] is None or en < timing[P.index(p)]:
                        timing[P.index(p)] = en

            print(timing)
        l.append(timing)
        timing = [None for i in range(len(P))]

    plt.plot(P, l[0], P, l[1], P, l[2])
    plt.xlabel(r'$p$')
    plt.ylabel(r'$Time(sec)$')
    plt.title(r'Вариация параметра p')
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    test_fix_Q()
    #test_fix_e()
    #test_fix_a()
    #test_fix_b()
    #test_fix_p()