def distance(s1, s2):
    l1 = len(s1)
    l2 = len(s2)
    if l1 == 1 and l2 == 1:  # if s1 and s2 is symbols
        if s1 == s2:  # and they match
            return 0
        else:
            return 1
    else:
        if (l1 > l2 == 1) or (l2 > l1 == 1):  # but if one of str is not a symbols
            return abs(l1 - l2) + 1  # return distance for N inserts + penalty

    t = 0
    if s1[-1] != s2[-1]:  # if the last symbols of strings aren't match
        t = 1

    return min(distance(s1[:l1 - 1], s2) + 1,
               distance(s1, s2[:l2 - 1]) + 1,
               distance(s1[:l1 - 1], s2[:l2 - 1]) + t)

if __name__ == "__main__":
    print(distance("метра", "матрица"))