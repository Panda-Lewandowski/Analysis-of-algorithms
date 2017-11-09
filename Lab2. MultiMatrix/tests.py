from random import randint
from time import time
from classic_multi_matrix import classic_multi
from imprv_classic_multi_matrix import imprv_classic_multi
from winograd_multi_matrix import winograd_multi
from imprv_winograd_multi_matrix import imprv_winograd_multi


TIMES = 3


def random_matrix(n, m):
    return [[randint(0, 100) for i in range(m)] for j in range(n)]


def time_testing():
    print('...TIMING...\n\n')

    with open('log.txt', 'w') as f:

        f.write("Size      | Classic   | Winorgad  | Imprv Wino   | Impv Classic\n")

        for size in range(100, 1100, 100):

            print('Multiplication of matrix {0} X {0} '.format(size))

            f.write("{0} X {0} |".format(size))

            a = random_matrix(size, size)
            b = random_matrix(size, size)

            t1, t2, t3, t4 = 0, 0, 0, 0

            for i in range(TIMES):

                start = time()
                res_class = classic_multi(a, b)
                stop = time()

                t1 += (stop - start)

                start = time()
                res_wino = winograd_multi(a, b)
                stop = time()

                t2 += (stop - start)

                start = time()
                res_wino_imprv = imprv_winograd_multi(a, b)
                stop = time()

                t3 += (stop - start)

                start = time()
                res_imprv = imprv_classic_multi(a, b)
                stop = time()

                t4 += (stop - start)

            f.write(" {0:<.5f}   | {1:<.5f}   | {2:<.5f}      | {3:<.5f}\n".format(t1 * 1000/TIMES, t2 * 1000/TIMES,
                                                             t3 * 1000/TIMES, t4 * 1000/TIMES))

        for size in range(100, 1100, 100):
                size += 1

                print('Multiplication of matrix {0} X {0} '.format(size))

                f.write("{0} X {0} |".format(size))

                a = random_matrix(size, size)
                b = random_matrix(size, size)

                t1, t2, t3, t4 = 0, 0, 0, 0

                for i in range(TIMES):
                    start = time()
                    res_class = classic_multi(a, b)
                    stop = time()

                    t1 += (stop - start)

                    start = time()
                    res_wino = imprv_winograd_multi(a, b)
                    stop = time()

                    t2 += (stop - start)

                    start = time()
                    res_wino_imprv = imprv_winograd_multi(a, b)
                    stop = time()

                    t3 += (stop - start)

                    start = time()
                    res_imprv = imprv_classic_multi(a, b)
                    stop = time()

                    t4 += (stop - start)

                f.write(" {0:<.5f}   | {1:<.5f}   | {2:<.5f}      | {3:<.5f}\n".format(t1 * 1000 / TIMES, t2 * 1000 / TIMES,
                                                                 t3 * 1000 / TIMES, t4 * 1000 / TIMES))

    print('...end...\n\n')


if __name__ == '__main__':
    time_testing()
