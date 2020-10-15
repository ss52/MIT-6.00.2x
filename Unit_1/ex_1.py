class Item(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = float(v)
        self.weight = float(w)

    def getName(self):
        return self.name

    def getValue(self):
        return self.value

    def getWeight(self):
        return self.weight

    def __str__(self):
        return '<' + self.name + ', ' + str(self.value) + ', ' + str(self.weight) + '>'


def buildItems():
    # items = (('clock', 175, 10), ('painting', 90, 9), ('radio', 20, 4), #('vase', 50, 2), ('book', 10, 1), ('computer', 200, 20))
    items = (('clock', 175, 10), ('painting', 90, 9), ('radio', 20, 4))
    return [Item(n, v, w) for n, v, w in items]


# generate all combinations of N items
def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        combo = []
        for j in range(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo


def yieldAllCombos(items):
    """
      Generates all combinations of N items into two bags, whereby each
      item is in one or zero bags.

      Yields a tuple, (bag1, bag2), where each bag is represented as
      a list of which item(s) are in each bag.
    """
    N = len(items)
    # enumerate the 3**N possible combinations
    for i in range(3**N):
        bag_1 = []
        bag_2 = []
        for j in range(N):
            if (i // 3**j) % 3 == 0:
                bag_1.append(items[j])
            elif (i // 3**j) % 3 == 1:
                bag_2.append(items[j])
        yield (bag_1, bag_2)


items = buildItems()
for combo in yieldAllCombos(items):
    print("bag 1:")
    for elem in combo[0]:
        print("  ", elem.getName())
    print("bag 2:")
    for elem in combo[1]:
        print("  ", elem.getName())
    print("*" * 10)
