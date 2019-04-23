def total(a: int, b: int) -> int:
    """
    Returns int, as sum a and b

    >>> total(1, 5)
    6

    >>> total(4, 6)
    10

    >>> total(1, 2)
    3

    >>> total(1, 4)
    5

    >>> total(17, 5)
    22

    :param a:
    :param b:
    :rtype int:
    """

    if not isinstance(a, int):
        raise Exception('a not type int')
    if not isinstance(b, int):
        raise Exception('b not type int')
    return a + b
