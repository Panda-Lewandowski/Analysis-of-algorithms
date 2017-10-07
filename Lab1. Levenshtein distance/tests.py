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
    pass


if __name__ == "__main__":
    result_test()