#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the utopianTree function below.
def utopianTree_Loop(n):
    height = 1

    for i in range(1, n+1):
        if (i % 2 == 0):
            height += 1
        else:
            height = height * 2

    return height

def utopianTree_function_loop(n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return int(2 ** ((n/2)+1) - 1)
    elif n % 2 == 1:
        return int(2 ** (((n+1)/2)+1) - 2)

def utopianTree(n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return 2 ** ((n/2)+1) - 1
    elif n % 2 == 1:
        return 2 ** (((n+1)/2)+1) - 2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
