def num_buses(n):
    """ (int) -> int

    Precondition: n >= 0

    Return the minimum number of buses required to transport n people.
    Each bus can hold 50 people.
    """

    if n == 0:
        return n

    elif n % 50 == 0:
        return n // 50

    else:
        return n // 50 + 1
        
def stock_price_summary(price_changes):
    """ (list of number) -> (number, number) tuple

    price_changes contains a list of stock price changes. Return a 2-item
    tuple where the first item is the sum of the gains in price_changes and
    the second is the sum of the losses in price_changes.
    """

    sum_gains = 0
    sum_losses = 0

    for item in price_changes:
        if item > 0:
            sum_gains += item
        else:
            sum_losses += item
    return sum_gains, sum_losses


# print(stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01]))


def swap_k(L, k):
    """ (list, int) -> NoneType

    Precondtion: 0 <= k <= len(L) // 2

    Swap the first k items of L with the last k items of L.

	"""

    # L[:k], L[-k:] = L[-k:], L[:k]  # WRONG

    for i in range(k):
        L[i], L[i + len(L) - k] = L[i + len(L) - k], L[i]  # multiple assignment


if __name__ == '__main__':
    import doctest
    doctest.testmod()
