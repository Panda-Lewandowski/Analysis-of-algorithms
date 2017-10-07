def distance(s1, s2):
    l1 = len(s1)
    l2 = len(s2)

    row1 = [x for x in range(l2 + 1)]  # we need only two rows
    row2 = [1]  # the first row and column will be like [0, 1, ... n] and intersect at 0
    # print(row1)

    for i in range(1, l1 + 1):  # loop through rows
        for j in range(1, len(row1)):  # loop through column
            if s1[i - 1] != s2[j - 1]:  # if symbols doesn't match
                row2.append(min(row1[j] + 1,   # there are three variants
                                row2[j - 1] + 1,
                                row1[j - 1] + 1))
            else:
                row2.append(min(row1[j] + 1,  # there are three variants
                                row2[j - 1] + 1,
                                row1[j - 1]))  # if match

        # print(row2)
        row1 = row2  # change rows
        row2 = [i + 1]

    return row1[-1]  # return the lower right value matrix


if __name__ == "__main__":
    print(distance("ме", "м"))
