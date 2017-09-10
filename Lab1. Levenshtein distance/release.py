import base as bs
import modified as md
import base_with_rec as rec

if __name__ == "__main__":
    print("Введите два слова через пробел:")
    s = input()
    s1, s2 = s.split()
    print("Расстояние Левенштейна между двумя введенными словами: ", bs.distance(s1, s2),
          md.distance(s1, s2),
          rec.distance(s1, s2))

