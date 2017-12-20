import numpy as np
import random as rnd

MAX_DIS = 10  # maximum distance
MIN_DIS = 1  # minimum distance


def fill_dis_matr(n):
    m = np.zeros((n, n))
    for i in range(n):
        for j in range(i+1, n):
            t = rnd.randint(MIN_DIS, MAX_DIS)
            m[i][j], m[j][i] = t, t
    return m


m = 15  # amount of ants and cities
e = 2  # amount of elite ants

a = 2    # coefficient of strengthen the sense of smell
b = 1  # coefficient of strengthen of desire
Q = MIN_DIS * m  # coefficient of the alleged best way
t_max = 200   # the amount of "generations"
p = 0.5  # coefficient of evaporation


def aco(m, e, d, t_max, alpha, beta, q):
    nue = 1 / d  # matrix of desire
    teta = np.random.sample((m, m))  # init ferromon paths, here may be np.zeros((m,m))
    T_min = None  # min path
    L_min = None  # min len of path

    t = 0  # the first "generation"

    while t < t_max:
        teta_k = np.zeros((m, m))

        for k in range(m):  # for each ant, who are in its own town
            Tk = [k]
            Lk = 0
            i = k   # current town

            while len(Tk) != m:
                J = [r for r in range(m)]   # generate possible to visit towns
                for c in Tk:  # remove visited towns
                    J.remove(c)

                P = [0 for a in J]  # probability that ant select a-town

                for j in J:
                    if d[i][j] != 0:  # if the path exist
                        buf = sum((teta[i][l] ** alpha) * (nue[i][l] ** beta) for l in J)
                        P[J.index(j)] = (teta[i][j] ** alpha) * (nue[i][j] ** beta) / buf
                    else:
                        P[J.index(j)] = 0

                Pmax = max(P)
                if Pmax == 0:  # if all paths are zero, it's signal that ant is isolated
                    break

                index = P.index(Pmax)  # index of selected town
                Tk.append(J[index])   # add town to way
                Lk += d[i][J[index]]  # add distance
                i = J.pop(index)  # go to selected town

            if L_min is None or (Lk + d[Tk[0]][Tk[-1]]) < L_min:  # check that it's not minimum,
                L_min = Lk + d[Tk[0]][Tk[-1]]                    # do not forget about the way back
                T_min = Tk

            for g in range(len(Tk) - 1):   # update ferromons path
                a = Tk[g]
                b = Tk[g + 1]
                teta_k[a][b] += q / Lk

        teta_e = (e * Q / L_min) if L_min else 0   # elite ants
        teta = (1 - p) * teta + teta_k + teta_e     # update ferromons after generation
        t += 1

    return T_min, L_min


if __name__ == "__main__":
    D = fill_dis_matr(m)  # matrix of distance
    print(D)
    print(aco(m, e, D, t_max, a, b, Q))
