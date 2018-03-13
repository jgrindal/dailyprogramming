#!/bin/python3

import sys
import os


# Complete the function below.

def swap(a, l, r):
    temp = a[l]
    a[l] = a[r]
    a[r] = temp
    return a


def moves(a):
    a.pop(0)
    l = 0
    r = len(a) - 1
    swaps = 0

    while True:
        for num in a:
            if num % 2 == 1:
                l += 1
            else:
                break
        for num in reversed(a):
            if num % 2 == 0:
                r -= 1
            else:
                break
        if r < l:
            break
        a = swap(a, l, r)
        swaps += 1
    return swaps

print(moves([4, 13, 10, 21, 20]))
