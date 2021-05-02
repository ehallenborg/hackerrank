#!/bin/python3

import math
import os
import random
import re
import sys

'''
Every time you give a loaf of bread to some person i, you must also give a loaf of bread to the person immediately in front of or behind them in the line (i.e., i+1 or i-1 ).
After all the bread is distributed, each person must have an even number of loaves.
'''

# Complete the fairRations function below.
def fairRations(B):
    bread = 0

    for i in range(len(B)-1):
        if B[i] % 2 != 0:
            B[i+1] += 1
            bread += 2

    return bread if B[-1]%2 == 0 else 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)

    fptr.write(str(result) + '\n')

    fptr.close()
