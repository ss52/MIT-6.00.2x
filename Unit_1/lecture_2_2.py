def fastFib(n, memo={}):
    """
    Вычисляем число Фибонначи от n
    В словарь memo будем добавлять уже вычисленные значения чисел Фибонначи
    """
    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = fastFib(n - 1, memo) + fastFib(n - 2, memo)
        memo[n] = result
        return result
