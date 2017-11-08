from random import randint
from time import time
from classic_multi_matrix import classic_multi
from imprv_classic_multi_matrix import imprv_classic_multi
from winograd_multi_matrix import winograd_multi


def random_matrix(n, m):
    return [[randint(0, 100) for i in range(m)] for j in range(n)]


def time_testing():
    print('...TIMING...\n\n')

    print("5 X 5\n")

    a = random_matrix(20, 20)
    b = random_matrix(20, 20)

    t1, t2, t3 = 0, 0, 0

    for i in range(100):

        start = time()
        res_class = classic_multi(a, b)
        stop = time()

        t1 += (stop - start)

        start = time()
        res_wino = winograd_multi(a, b)
        stop = time()

        t2 += (stop - start)

        start = time()
        res_imprv = imprv_classic_multi(a, b)
        stop = time()

        t3 += (stop - start)

    print("Classic multiplication of matrix: {0:f} sec\n"
          "Winorgad multiplication of matrix: {1:f} sec\n"
          "Imporove classic multiplication of matrix: {2:f} sec\n"
          "Are result matrix equivalent? {3}".format(t1 * 10, t2 * 10, t3 * 10, res_class == res_wino))

    print("\n\n20 X 20\n")

    a = random_matrix(20, 20)
    b = random_matrix(20, 20)

    t1, t2, t3 = 0, 0, 0

    for i in range(100):
        start = time()
        res_class = classic_multi(a, b)
        stop = time()

        t1 += (stop - start)

        start = time()
        res_wino = winograd_multi(a, b)
        stop = time()

        t2 += (stop - start)

        start = time()
        res_imprv = imprv_classic_multi(a, b)
        stop = time()

        t3 += (stop - start)

    print("Classic multiplication of matrix: {0:f} sec\n"
          "Winorgad multiplication of matrix: {1:f} sec\n"
          "Imporove classic multiplication of matrix: {2:f} sec\n"
          "Are result matrix equivalent? {3}".format(t1 * 10, t2 * 10, t3 * 10, res_class == res_wino))

    print("\n\n40 X 40\n")

    a = random_matrix(130, 130)
    b = random_matrix(130, 130)

    t1, t2, t3 = 0, 0, 0

    for i in range(100):
        start = time()
        res_class = classic_multi(a, b)
        stop = time()

        t1 += (stop - start)

        start = time()
        res_wino = winograd_multi(a, b)
        stop = time()

        t2 += (stop - start)

        start = time()
        res_imprv = imprv_classic_multi(a, b)
        stop = time()

        t3 += (stop - start)

    print("Classic multiplication of matrix: {0:f} msec\n"
          "Winorgad multiplication of matrix: {1:f} msec\n"
          "Imporove classic multiplication of matrix: {2:f} sec\n"
          "Are result matrix equivalent? {3}".format(t1 * 10, t2 * 10, t3 * 10, res_class == res_wino))


if __name__ == '__main__':
    time_testing()
