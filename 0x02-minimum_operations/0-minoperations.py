#!/usr/bin/python3
""" 0-minoperations """


def minOperations(n):
    """
    Calculates the minimum number of operations to get n 'H' characters.

    Returns:
        int: Minimum number of operations, or 0 if impossible.
    """
    if n < 2:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
