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


def noReplacementSimulation(numTrials):
    res = 0

    for trial in range(numTrials):
        bag = [0, 0, 0, 1, 1, 1]
        sum = 0
        for i in range(3):
            ball_number = random.randint(0, len(bag) - 1)
            ball = bag.pop(ball_number)
            sum += ball

        if sum == 3 or sum == 0:
            res += 1

    return res / numTrials


# print(noReplacementSimulation(5000))
