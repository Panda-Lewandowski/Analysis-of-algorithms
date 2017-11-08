import classic_multi_matrix

def winograd_multi(G, H):
    a = len(G)
    b = len(H)
    c = len(H[0])

    if b != len(G[0]):
        print("Different dimension of the matrics")
        return

    d = b // 2

    row_factor = [0 for i in range(a)]
    col_factor = [0 for i in range(c)]

    # Row Factor calc
    for i in range(a):
        row_factor[i] = sum(G[i][2 * j] * G[i][2 * j + 1] for j in range(d))

    # Col Factor calc
    for i in range(c):
        col_factor[i] = sum(H[2 * j][i] * H[2 * j + 1][i] for j in range(d))

    answer = [[0 for i in range(c)] for j in range(a)]
    for i in range(a):
        for j in range(c):
            answer[i][j] = sum((G[i][2 * k] + H[2 * k + 1][j]) * (G[i][2 * k + 1] + H[2 * k][j]) for k in range(d))\
                           - row_factor[i] - col_factor[j]


    # For odd matrix
    if b % 2:
        for i in range(a):
            answer[i][j] = sum(G[i][b - 1] * H[b - 1][j] for j in range(c))

    return answer


if __name__ == "__main__":
    A = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]
    B = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8]]
    print(winograd_multi(A, B))
    print(classic_multi_matrix.classic_multi(A, B))
