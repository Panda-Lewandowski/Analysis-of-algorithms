def imprv_classic_multi(A, B):
    if len(B) != len(A[0]):
        print("Different dimension of the matrics")
        return
    return [[sum(x * B[i][col] for i, x in enumerate(row)) for col in range(len(B[0]))] for row in A]


if __name__ == "__main__":
    A = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]
    B = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8]]

