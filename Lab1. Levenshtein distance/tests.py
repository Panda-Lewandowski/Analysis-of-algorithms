import base as bs
import modified as md
import base_with_rec as rec
from itertools import combinations
import time

def test():
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
    t1, t2, t3 = 0, 0, 0
    times = 0
    print("Расстояние Левенштейна между строками:\n")
    for i in combinations(l, 2):
        times += 1

        start = time.time()
        a = bs.distance(i[0], i[1])
        stop = time.time()

        t1 += (stop - start)

        start = time.time()
        b = md.distance(i[0], i[1])
        stop = time.time()

        t2 += (stop - start)

        start = time.time()
        c = rec.distance(i[0], i[1])
        stop = time.time()

        t3 += (stop - start)

        print(i[0], "   ", i[1], ":  ", a, " ", b, " ", c, " ")

    print("Среднее время:\n")
    print("Базовый: {0:.10f}".format(t1 / times))
    print("Модифицированный:  {0:.10f}".format(t2 / times))
    print("Базовый с рекурсией:  {0:.10f}".format(t3 / times))

if __name__ == "__main__":
    test()