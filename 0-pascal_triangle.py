#!/usr/bin/python3
""" 0-pascal_triangle.py """


def pascal_triangle(n):
    """ returns a list of lists of integers representing
    the Pascal’s triangle of n """
    triangle = []

    if n <= 0:
        return []

    for i in range(n - 1):
        if i == 0:
            triangle.append([1])
        prev = triangle[-1]
        row = [1]

        for j in range(len(prev) - 1):
            row.append(prev[j] + prev[j + 1])
        row.append(1)
        triangle.append(row)
    return triangle
