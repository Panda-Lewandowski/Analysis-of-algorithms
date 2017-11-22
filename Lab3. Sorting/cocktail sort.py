import random
import time

N = 10_000
TIMES = 10


def std_cocktail_sort (x):
    left = 0
    right = len(x)-1

    while left <= right:
        for i in range(left, right):
            if x[i] > x[i+1]:
                x[i], x[i+1] = x[i+1], x[i]
        right = right - 1

        for i in range(right, left, -1):
            if x[i-1] > x[i]:
                x[i-1], x[i] = x[i], x[i-1]
        left = left + 1

    return x


def opt_cocktail_sort(x):
    for i in range(len(x)//2):
        swap = False
        for j in range(1+i, len(x)-i):
            if x[j] < x[j-1]:
                x[j], x[j - 1] = x[j - 1], x[j]
                swap = True
        if not swap:
            break
        swap = False
        for j in range(len(x)-i-1, i, -1):
            if x[j] < x[j-1]:
                x[j], x[j - 1] = x[j - 1], x[j]
                swap = True
        if not swap:
            break

    return x


if __name__ == "__main__":
    a = []
    b = []
    c = []
    for i in range(N):
        a.append(i)
        b.append(N-i)
        c.append(random.randint(-N, N))

    print("NO OPTIMIZED std_cocktail_sort(x)")

    print("\n...SORTING ARRAY...")
    st = time.time()
    na = std_cocktail_sort(a)
    end = time.time()
    print("\nTIME:", (end - st), "  sec")

    print("\n...REVERSE ARRAY...")
    st = time.time()
    nb = std_cocktail_sort(b)
    end = time.time()
    print( "\nTIME:", (end - st), "  sec")

    print("\n...RANDOM ARRAY...")
    st = time.time()
    nc = std_cocktail_sort(c)
    end = time.time()
    print("\nTIME:", (end - st), "  sec")

    print("\n\nOPTIMIZED opt_cocktail_sort(x)")

    print("\n...SORTING ARRAY...")
    st = time.time()
    na = opt_cocktail_sort(a)
    end = time.time()
    print("\nTIME:", (end - st), "  sec")

    print("\n...REVERSE ARRAY...")
    st = time.time()
    nb = opt_cocktail_sort(b)
    end = time.time()
    print("\nTIME:", (end - st), "  sec")

    print("\n...RANDOM ARRAY...")
    st = time.time()
    nc = opt_cocktail_sort(c)
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
    #         std_cocktail_sort(a)
    #         end = time.time()
    #
    #         sa += (end - st) * 1000
    #
    #         st = time.time()
    #         std_cocktail_sort(b)
    #         end = time.time()
    #
    #         sb += (end - st) * 1000
    #
    #         st = time.time()
    #         std_cocktail_sort(c)
    #         end = time.time()
    #
    #         sc += (end - st) * 1000
    #
    #         st = time.time()
    #         opt_cocktail_sort(a)
    #         end = time.time()
    #
    #         oa += (end - st) * 1000
    #
    #         st = time.time()
    #         opt_cocktail_sort(b)
    #         end = time.time()
    #
    #         ob += (end - st) * 1000
    #
    #         st = time.time()
    #         opt_cocktail_sort(c)
    #         end = time.time()
    #
    #         oc += (end - st) * 1000
    #
    #     print("\hline \n {0} & {1:.3f} | {2:.3f}  & {3:.3f} | {4:.3f} &"
    #           " {5:.3f} | {6:.3f}\\\\".format(i, sa/TIMES, oa/TIMES,
    #                                           sb/TIMES, ob/TIMES, sc/TIMES, oc/TIMES))