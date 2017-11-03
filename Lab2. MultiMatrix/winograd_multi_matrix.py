import classic_multi_matrixdef winograd_multi(G, H):    a = len(G)    b = len(H)    c = len(H[0])    if b != len(G[0]):        print("Different dimension of the matrics")        return    d = b // 2    row_factor = [0] * a    col_factor = [0] * c    # Row Factor calc    for i in range(a):        for j in range(d):            row_factor[i] += G[i][2 * j] * G[i][2 * j + 1]    # Col Factor calc    for i in range(c):        for j in range(d):            col_factor[i] += H[2 * j][i] * H[2 * j + 1][i]    tmp = []    # Ans calc    for i in range(a):  # FIXME        answer = []        for j in range(c):            buf = - row_factor[i] - col_factor[j]            for k in range(d):                buf += (G[i][2 * k] + H[2 * k + 1][j]) * (G[i][2 * k + 1] + H[2 * k][j])            answer.append(buf)        tmp.append(answer)    foo = [[0] * c] * a    for i in range(a):  # FIXME        for j in range(c):            foo[i][j] = - row_factor[i] - col_factor[j]            for k in range(d):                foo[i][j] += (G[i][2 * k] + H[2 * k + 1][j]) * (G[i][2 * k + 1] + H[2 * k][j])    print(foo)    # For odd matrix    if b % 2:        for i in range(a):            for j in range(c):                tmp[i][j] += G[i][b - 1] * H[b - 1][j]    return tmp# http://ru.math.wikia.com/wiki/Алгоритм_Копперсмита_—_Виноградаif __name__ == "__main__":    A = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]    B = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8]]    print(winograd_multi(A, B))    print(classic_multi_matrix.classic_multi(A, B))