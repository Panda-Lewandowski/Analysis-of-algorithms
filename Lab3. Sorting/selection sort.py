import random
import time

N = 10000
TIMES = 10


def std_selection_sort(x):
    for i in range(len(x)):
        min_ind = i
        for j in range(i, len(x)):
            if x[min_ind] > x[j]:
                min_ind = j
        x[i], x[min_ind] = x[min_ind], x[i]

    return x


def opt_selection_sort(x):
    for i, e in enumerate(x):
        mn = min(range(i, len(x)), key=x.__getitem__)
        x[i], x[mn] = x[mn], e
    return x


if __name__ == "__main__":
    a = []
    b = []
    c = []
    for i in range(N):
        a.append(i)
        b.append(N - i)
        c.append(random.randint(-N, N))

    print("NO OPTIMIZED std_shell_sort(x)")

    print("\n...SORTING ARRAY...")
    st = time.time()
    na = std_selection_sort(a)
    end = time.time()
    print("\nTIME:", (end - st), "  sec")

    print("\n...REVERSE ARRAY...")
    st = time.time()
    nb = std_selection_sort(b)
    end = time.time()
    print("\nTIME:", (end - st), "  sec")

    print("\n...RANDOM ARRAY...")
    st = time.time()
    nc = std_selection_sort(c)
    end = time.time()
    print("\nTIME:", (end - st), "  sec")

    print("\n\nOPTIMIZED opt_shell_sort(x)")

    print("\n...SORTING ARRAY...")
    st = time.time()
    na = opt_selection_sort(a)
    end = time.time()
    print("\nTIME:", (end - st), "  sec")

    print("\n...REVERSE ARRAY...")
    st = time.time()
    nb = opt_selection_sort(b)
    end = time.time()
    print("\nTIME:", (end - st), "  sec")

    print("\n...RANDOM ARRAY...")
    st = time.time()
    nc = opt_selection_sort(c)
    end = time.time()
    print("\nTIME:", (end - st), "  sec")

    # for i in range(N, 1100, 100):
    #     a = []
    #     b = []
    #     c = []
    #     for k in range(i):
    #         a.append(k)
    #         b.append(i - k)
    #         c.append(random.randint(-i, i))
    #
    #     sa, sb, sc, oa, ob, oc = 0, 0, 0, 0, 0, 0
    #
    #     for j in range(TIMES):
    #         st = time.time()
    #         std_selection_sort(a)
    #         end = time.time()
    #
    #         sa += (end - st) * 1000
    #
    #         st = time.time()
    #         std_selection_sort(b)
    #         end = time.time()
    #
    #         sb += (end - st) * 1000
    #
    #         st = time.time()
    #         std_selection_sort(c)
    #         end = time.time()
    #
    #         sc += (end - st) * 1000
    #
    #         st = time.time()
    #         opt_selection_sort(a)
    #         end = time.time()
    #
    #         oa += (end - st) * 1000
    #
    #         st = time.time()
    #         opt_selection_sort(b)
    #         end = time.time()
    #
    #         ob += (end - st) * 1000
    #
    #         st = time.time()
    #         opt_selection_sort(c)
    #         end = time.time()
    #
    #         oc += (end - st) * 1000
    #
    #     print("\hline \n {0} & {1:.3f} | {2:.3f}  & {3:.3f} | {4:.3f} &"
    #           " {5:.3f} | {6:.3f}\\\\".format(i, sa/TIMES, oa/TIMES,
    #                                           sb/TIMES, ob/TIMES, sc/TIMES, oc/TIMES))
    #
