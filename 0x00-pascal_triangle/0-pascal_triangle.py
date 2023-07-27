#!/usr/bin/python3
"""Pascal triangle"""


def pascal_triangle(n):
    """Returns a list of lists of integers
    representing the Pascal’s triangle of n:
    """

    if n <= 0:
        return []

    """ initialize an empty resulting array """
    triangle = [[] for idx in range(n)]

    for i in range(n):
        for col in range(i+1):
            if(col < i):
                if(col == 0):
                    """ the first column is always set to 1 """
                    triangle[i].append(1)
                else:
                    triangle[i].append(triangle[i-1][col]
                                       + triangle[i-1][col-1])
            elif(col == i):
                """ the diagonal is always set to 1 """
                triangle[i].append(1)

    return triangle
