from itertools import starmap
from operator import mul
from random import randint
import time
import asyncio
import logging
from concurrent.futures import ThreadPoolExecutor

logging.basicConfig(format="[%(thread)-5d]%(asctime)s: %(message)s")
logger = logging.getLogger('async')
logger.setLevel(logging.INFO)
loop = asyncio.get_event_loop()  # event loop
executor = ThreadPoolExecutor(max_workers=9)  # thread pool


def multi(A, B):
    if len(B) != len(A[0]):
        print("Different dimension of the matrics")
        return

    n = len(A)
    m = len(A[0])
    t = len(B[0])

    answer = [[0 for i in range(t)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            for k in range(t):
                answer[i][k] += A[i][j] * B[j][k]
    return answer


async def get_new_elem(row, tmp):
    return [sum(starmap(mul, zip(row, column))) for column in tmp]


async def multi_async(A, B):
    tmp = tuple(zip(*B))

    results = await asyncio.gather(*[get_new_elem(row, tmp) for row in A])
    return results


def random_matrix(n, m):
    return [[randint(0, 100) for i in range(m)] for j in range(n)]


def main(A, B):
    if len(B) != len(A[0]):
        print("Different dimension of the matrics")
        return

    start_time = time.time()
    result = loop.run_until_complete(multi_async(A, B))
    logger.info("Completed in {} seconds".format(time.time() - start_time))
    return result


if __name__ == '__main__':
    A = random_matrix(300, 300)
    B = random_matrix(300, 300)
    # A = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]
    # B = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8]]
    C1 = main(A, B)
    st = time.time()
    C2 = multi(A, B)
    print(time.time() - st)
    print(C1 == C2)
