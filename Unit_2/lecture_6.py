# Random walk alrogitm
#
# Нужно три функции:
# 1) Симуляция одного шага
# 2) Повтор шагов N раз и запись состояний
# 3) Результаты и графика
import random


class Location(object):
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def move(self, deltaX: float, deltaY: float):
        return Location(self.x + deltaX, self.y + deltaY)

    def getX(self) -> float:
        return self.x

    def getY(self) -> float:
        return self.y

    def distFrom(self, other):
        ox = other.x
        oy = other.y
        xDist = self.x - ox
        yDist = self.y - oy
        return (xDist ** 2 + yDist ** 2) ** 0.5

    def __str__(self) -> str:
        return "<" + str(self.x) + "," + str(self.y) + ">"


class Field(object):
    def __init__(self) -> None:
        self.drunks = {}  # так как мы будет делать класс drunk ключом словаря, он должен быть хэшируемым

    def addDrunk(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError('Duplicate drunk')
        else:
            self.drunks[drunk] = loc

    def getLoc(self, drunk):
        if drunk not in self.drunks:
            raise ValueError("No such drunk")
        else:
            return self.drunks[drunk]

    def moveDrunk(self, drunk):
        if drunk not in self.drunks:
            raise ValueError("No such drunk")
        else:
            xDist, yDist = drunk.takeStep()
            currentLocation = self.drunks[drunk]
            self.drunks[drunk] = currentLocation.move(xDist, yDist)


class Drunk(object):
    def __init__(self, name) -> None:
        self.name = name

    def __str__(self) -> str:
        return 'This drunk is named ' + self.name


class UsualDrunk(Drunk):
    def takeStep(self):
        stepCoices = [(0.0, 1.0), (0.0, -1.0), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepCoices)


class ColdDrunk(Drunk):
    def takeStep(self):
        stepCoices = [(0.0, 0.9), (0.0, -1.1), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepCoices)
