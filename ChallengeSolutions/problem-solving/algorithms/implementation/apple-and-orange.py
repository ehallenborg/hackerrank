#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
# I have two different ways - a short way to print the result
# and a more verbose way that shows the answer step-by-step

def short_and_sweet(s, t, a, b, apples, oranges):
    print(sum([1 for x in apples if (x + a) >= s and (x + a) <= t]))
    print(sum([1 for x in oranges if (x + b) >= s and (x + b) <= t]))

def countApplesAndOranges(s, t, a, b, apples, oranges):
    dropped_apples = 0
    dropped_oranges = 0

    for i in apples:
        if ((i+a) >= s and (i+a) <= t):
            dropped_apples += 1

    for j in oranges:
        if ((j+b) >= s and (j+b) <= t):
            dropped_oranges += 1

    print(dropped_apples)
    print(dropped_oranges)

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
    #short_and_sweet(s, t, a, b, apples, oranges)

