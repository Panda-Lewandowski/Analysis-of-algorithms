from itertools import starmap
from operator import mul
import concurrent.futures
from random import randint
from time import time


def multi(A, B):
    if len(B) != len(A[0]):
        print("Different dimension of the matrics")
        return

    tmp = tuple(zip(*B))

    result = []

    for row in A:
        result.append([sum(starmap(mul, zip(row, column))) for column in tmp])

    return result


def multi_multiproc(A, B):
    if len(B) != len(A[0]):
        print("Different dimension of the matrics")
        return

    tmp = tuple(zip(*B))

    result = []

    executor = concurrent.futures.ThreadPoolExecutor(max_workers=64)

    for row in A:
        executor.submit(result.append, [sum(starmap(mul, zip(row, column))) for column in tmp])
    
    executor.shutdown()

    return result


def random_matrix(n, m):
    return [[randint(0, 100) for i in range(m)] for j in range(n)]


if __name__ == '__main__':
    a = random_matrix(40, 40)
    b = random_matrix(40, 40)

    t1, t2 = 0, 0

    start = time()
    res_class = multi_multiproc(a, b)
    stop = time()

    t1 += (stop - start)

    start = time()
    res_wino = multi(a, b)
    stop = time()

    t2 += (stop - start)

    print(t1, t2, res_class == res_wino)