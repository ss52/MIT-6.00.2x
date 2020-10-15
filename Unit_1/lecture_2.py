from lecture_1 import buildMenu, Food
import random


def maxVal(toConsider, avail):
    """ Реализация дерева поиска (Search tree alg)
        toConsider - список предметов еще не использованных
        avail - свободное место (функция используется рекурсивно)
        Реузльтат - кортеж максимальная ценность и предметы
    """
    if toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0].getCost() > avail:
        result = maxVal(toConsider[1:], avail)
    else:
        nextItem = toConsider[0]
        # левая ветка дерева
        withVal, withToTake = maxVal(toConsider[1:], avail - nextItem.getCost())
        withVal += nextItem.getValue()
        # правая ветка дерева
        withoutVal, withoutToTake = maxVal(toConsider[1:], avail)
        # выбираем лучшую ветку
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)

    return result


def fastMaxVal(toConsider, avail, memo={}):
    """ Реализация дерева поиска (Search tree alg) с памятью
        toConsider - список предметов еще не использованных
        avail - свободное место (функция используется рекурсивно)
        memo - уже имеющиеся результаты по оставшимся предметал и оставшемуся месту
        Реузльтат - кортеж максимальная ценность и предметы
    """
    if (len(toConsider), avail) in memo:
        result = memo[(len(toConsider), avail)]
    elif toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0].getCost() > avail:
        result = fastMaxVal(toConsider[1:], avail)
    else:
        nextItem = toConsider[0]
        # левая ветка дерева
        withVal, withToTake = fastMaxVal(toConsider[1:], avail - nextItem.getCost())
        withVal += nextItem.getValue()
        # правая ветка дерева
        withoutVal, withoutToTake = fastMaxVal(toConsider[1:], avail)
        # выбираем лучшую ветку
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)

    memo[(len(toConsider), avail)] = result
    return result


def buildLargeMenu(numItems, maxVal, maxCost):
    items = []
    for i in range(numItems):
        items.append(Food(str(i),
                          random.randint(1, maxVal),
                          random.randint(1, maxCost)))
    return items


def testMaxVal(foods, maxUnit, alg):
    print("Test brute force alg")
    print("Use search tree to allocate {} calories".format(maxUnit))
    val, taken = alg(foods, maxUnit)
    print('Total value of items taken =', val)
    for item in taken:
        print('   ', item)


def main():
    names = ['wine', 'beer', 'pizza', 'burger', 'fries', 'cola', 'apple', 'donut', 'cake']
    values = [89, 90, 95, 100, 90, 79, 50, 10]
    calories = [123, 154, 258, 354, 365, 150, 95, 195]

    foods = buildMenu(names, values, calories)
    testMaxVal(foods, 750, fastMaxVal)


if __name__ == "__main__":
    main()
