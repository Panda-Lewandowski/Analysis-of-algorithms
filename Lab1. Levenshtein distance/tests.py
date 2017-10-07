import base as bs
import modified as md
import base_with_rec as rec
from itertools import combinations
import time


def result_test():
    l = ["Январь",
         "Февраль",
         "Март",
         "Апрель",
         "Май",
         "Июнь",
         "Июль",
         "Август",
         "Сентябрь",
         "Октябрь",
         "Ноябрь",
         "Декабрь"]
    print("Расстояние Левенштейна между строками:\n")
    for i in combinations(l, 2):
        a = bs.distance(i[0], i[1])
        b = rec.distance(i[0], i[1])
        c = md.distance(i[0], i[1])

        # print(i[0], " &  ", i[1], "&  ", a, " ", b, " ", c, " & ", a, " ", b, " ", c, r" & V \\\hline")
        print(i[0], " -  ", i[1], ":  ", a, " ", b, " ", c)


def time_test():
    t1, t2, t3 = 0, 0, 0

    s1 = "aaaaaa"
    for i in range(10):
        s2 = "a" * (7 - i) + "b" * i

        for j in range(100):

            start = time.time()
            a = bs.distance(s1, s2)
            stop = time.time()

            t1 += (stop - start)

            start = time.time()
            b = md.distance(s1, s2)
            stop = time.time()

            t2 += (stop - start)

            start = time.time()
            c = rec.distance(s1, s2)
            stop = time.time()

            t3 += (stop - start)

        print("{0:f} {1:f} {2:f}    {3}{4}{5}".format(t1/100*1000, t2/100*1000, t3/100*1000, a, b, c))


if __name__ == "__main__":
    # result_test()
    time_test()