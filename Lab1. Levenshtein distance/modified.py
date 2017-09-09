def distance(s1, s2):
    d = None
    l1 = len(s1)
    l2 = len(s2)

    row1 = [x for x in range(l2 + 1)]
    row2 = [1]
    #print(row1)

    for i in range(1, l1 + 1):
        for j in range(1, len(row1)):
            if s1[i - 1] != s2[j - 1]:
                if j > 1 and s2[j - 2] == s1[i - 1]:
                    x = row1[j - 2] + 1
                    row2.append(min(row1[j] + 1,
                                    row2[j - 1] + 1,
                                    row1[j - 1] + 1, x))
                else:
                    row2.append(min(row1[j] + 1,
                                    row2[j - 1] + 1,
                                    row1[j - 1] + 1))
            else:
                row2.append(row1[j - 1])
        #print(row2)
        row1 = row2
        row2 = [i + 1]

    return row1[-1]


if __name__ == "__main__":
    print(distance("метра", "матрица"))
