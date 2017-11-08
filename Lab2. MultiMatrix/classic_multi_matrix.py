import numpy as np

def classic_multi(A, B):
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


if __name__ == "__main__":
    A = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]
    B = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8]]
    print(classic_multi(A, B))
