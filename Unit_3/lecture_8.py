# Определение числа пи методом Буфона-Лапласа. Бросаем иголки, в квадрат 2х2 в который вписан круг.
# Радиус круга 1, следовательно площать равна пи. Отноешние упавших иголок равно отношению площадей.
import random


def throwNeedles(numNeedles):
    inCircle = 0
    for needles in range(1, numNeedles + 1):
        x = random.random()
        y = random.random()

        if (x * x + y * y) ** 0.5 <= 0:
            inCircle += 1

    return 4 * (inCircle / float(numNeedles))
