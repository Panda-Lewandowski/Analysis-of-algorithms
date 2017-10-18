from itertools import starmap
from operator import mul


def classic_multi(A, B):
    return [[sum(x * B[i][col] for i, x in enumerate(row)) for col in range(len(B[0]))] for row in A]


def iprv_multi(A, B):
    """ Умножение матриц """

    if len(B) != len(A[0]):
        print("Облом!")
        return

    tmp = tuple(zip(*B))

    result = []

    for row in A:
        result.append([sum(starmap(mul, zip(row, column))) for column in tmp])

    return result


if __name__ == "__main__":
    A = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]
    B = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8]]
    print(classic_multi(A, B))
    print(iprv_multi(A, B))