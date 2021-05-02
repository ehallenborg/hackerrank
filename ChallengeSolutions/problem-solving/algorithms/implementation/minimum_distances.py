#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
# should add in a check for min_dist == 1 since that's the smallest distance possible
def minimumDistances(a):
    min_dist = len(a)

    for i in range(len(a)):
        if a.count(a[i]) > 1:
            for j in range(i+1, len(a)):
                if a[j] == a[i]:
                    min_dist = min(j - i, min_dist)

    return min_dist if min_dist < len(a) else -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
