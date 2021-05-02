#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the howManyGames function below.
def howManyGames(p, d, m, s):
    count = 0
    
    while s > m-1:
        if p > s:
            return count
        elif s >= p and count == 0:
            s = s - p
            p = p - d
            count += 1
        elif s >= p and p > m:
            s = s - p
            p = p - d
            count += 1
        elif s >= m:
            s = s - m
            count += 1

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    pdms = input().split()

    p = int(pdms[0])

    d = int(pdms[1])

    m = int(pdms[2])

    s = int(pdms[3])

    answer = howManyGames(p, d, m, s)

    fptr.write(str(answer) + '\n')

    fptr.close()
