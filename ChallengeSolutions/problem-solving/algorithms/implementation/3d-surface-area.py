#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the surfaceArea function below.
def surfaceArea(A):
    a = [[0] * (len(A[0]) + 2)]
    for row in A:
        a.append([0] + row + [0])
    a.append([0] * (len(A[0]) + 2))
    print(a)
    print(A)
    ans = len(A) * len(A[0]) * 2

    print(len(A))
    print(len(A[0]))
    print(len(a))

    for i in range(1, len(a)):
        for j in range(1, len(a[i])):
            ans += abs(a[i][j] - a[i-1][j])
            ans += abs(a[i][j] - a[i][j-1])
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    HW = input().split()

    H = int(HW[0])

    W = int(HW[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()
