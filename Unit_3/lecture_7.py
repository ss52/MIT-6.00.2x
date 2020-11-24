import numpy as np


def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    if len(L) == 0:
        return float('NaN')
    else:
        len_L = np.array([len(x) for x in L])
        mu = np.mean(len_L)
        sum2 = np.sum((len_L - mu) ** 2)
        return (sum2 / len(L)) ** 0.5


# print(stdDevOfLengths(['apples', 'oranges', 'kiwis', 'pineapples']))
