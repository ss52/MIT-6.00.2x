"""
Random walk alrogitm

Нужно три функции:
 1) Симуляция одного шага
 2) Повтор шагов N раз и запись состояний
 3) Результаты и графика

Вначале подготовим нектоорые абстракции:
Класс для хранения позиции - Location
Класс для самого объекта (Drunk) из которого унаследуем два: обычный и со смещенным перемещением.
Класс который свяжет объект с позицией - Field
"""
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


# Теперь перейдем к симуляции
def walk(f, d, numSteps: int) -> float:
    """
    f - Field
    d - Drunk in a field
    numSteps int >= 0
    Function move drunk numSteps times, return the distance between start and end location
    """
    start = f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)
    return start.distFrom(f.getLoc(d))


def simWalks(numSteps, numTrials, dClass):
    """
    numSteps int >= 0
    numTrials int >= 0
    dClass - subclass of Drunk
    Return list of final distances for each trial
    """
    Homer = dClass("Homer")
    origin = Location(0.0, 0.0)
    distances = []

    for t in range(numTrials):
        f = Field()
        f.addDrunk(Homer, origin)
        distances.append(round(walk(f, Homer, numSteps), 1))

    return distances


def drunkTest(walkLengths, numTrials, dClass):
    """
    walkLengths - sequence of int >=0
    numTrials int >= 0
    dClass - subclass of Drunk

    For each number of steps in walkLengths runs simWalk with numTrials
    """
    for numSteps in walkLengths:
        distances = simWalks(numSteps, numTrials, dClass)
        print(f'{dClass.__name__} random walk of {numSteps} steps')
        print(f'Mean = {round(sum(distances) / len(distances), 1)}')
        print(f'Max = {max(distances)}, Min = {min(distances)}')


random.seed(0)
drunkTest((10, 100, 1000, 10000), 100, ColdDrunk)
