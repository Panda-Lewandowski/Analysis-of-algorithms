def distance(s1, s2):
    l1 = len(s1)
    l2 = len(s2)
    if l1 == 1 and l2 == 1:
        if s1 == s2:
            return 0
        else:
            return 1
    else:
        if (l1 > l2 == 1) or (l2 > l1 == 1):
            return abs(l1 - l2)

    t = 0
    if s1[-1] != s2[-1]:
        t = 1

    return min(distance(s1[:l1 - 1], s2) + 1,
               distance(s1, s2[:l2 - 1]) + 1,
               distance(s1[:l1 - 1], s2[:l2 - 1]) + t)

if __name__ == "__main__":
    print(distance("метра", "матрица"))