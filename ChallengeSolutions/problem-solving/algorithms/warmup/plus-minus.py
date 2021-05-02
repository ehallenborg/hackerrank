#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    pos = 0
    neg = 0
    zero = 0

    for i in arr:
        if i > 0:
            pos += 1
        elif i < 0:
            neg += 1

    zero = arr.count(0)

    print(format(pos/len(arr), '.6f'))
    print(format(neg/len(arr), '.6f'))
    print(format(zero/len(arr), '.6f'))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
